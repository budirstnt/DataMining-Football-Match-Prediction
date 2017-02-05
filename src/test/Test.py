import src.application.MachineLearning.MachineLearningInput as MLInput
import src.application.MachineLearning.MachineLearningAlgorithm as MachineLearningAlgorithm


def doTest():
    matches, labels, matches_names = MLInput.get_datas()
    params = {"batch_size": 500, "number_step":1000}
    mag = MachineLearningAlgorithm.get_machine_learning_algorithm("TensorFlow", "KNN", matches, labels, matches_names, **params)

    mag.train()
    mag.score()


doTest()


