from bigml.api import BigML

if __name__ == "__main__":
  print "test"
  api = BigML("onidzelskyi", "a5b11ebe462ad583478cf40daf17e92060dc5915", dev_mode=True)
  source = api.create_source("./data/iris.csv")
  dataset = api.create_dataset(source)
  model = api.create_model(dataset)
  prediction = api.create_prediction(model,{"sepal length": 5, "sepal width": 2.5})
  api.pprint(prediction)
