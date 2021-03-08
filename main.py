from data_loaders.conv_data_generator import DataGenerator
from models.conv_model import ConvModel
from trainers.conv_model_trainer import ConvModelTrainer
from utils.config import process_config
from utils.dirs import create_dirs
from utils.utils import get_args
import warnings


def main():
    try:
        args = get_args()
        config = process_config(args.config)
    except Exception as err:
        print("missing or invalid arguments")
        exit(0)

    # # create the experiments dirs
    create_dirs([config.callbacks.tensor_board.log_dir, config.callbacks.checkpoint.dir])
    #

    data_generator = DataGenerator(config)
    print('Created the data generator.')

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = ConvModel(config)
    print('Created the model.')

    trainer = ConvModelTrainer(config, model.model)
    print('Created the trainer')

    print('Start training the model.')
    train = data_generator.get_train_data()
    valid = data_generator.get_valid_data()
    trainer.train(train, valid)

if __name__ == '__main__':
    main()