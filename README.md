# NeuralPipeline
**Automated** training of a convolutional neural network on the example of the problem of aircraft classification by image using **tensorflow**
The repository is a set of files with classes for automatic training and configuration files for them (config folder). 
Basic entities:
 * base - folder with abstract classes for datagenerator, model and trainer 
 * dataloaders - folder with data generators. Regulates the process of loading data, their preprocessing and determines in what form they will be submitted to the model
 * models - folder with models classes (CNO) and setup for them (transfer models, optimizers, regularizers)
 * trainers - folder with trainers for models. The trainer parameters regulate the training process of the model (fine-tuning stages, selection of callbacks, loss function, etc.)
 * callbacks - folder with users callbacks
 * plot - folder with user function for vizualization
 * utils - folder with modules to help the pipeline
 * config - folder with all settings for all part of pipeline
 
File main.py - entry point to the pipeline. Combines all parts of the pipeline into a single whole
