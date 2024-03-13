import numpy as np
import torch
from torchvision.models import resnet50, ResNet50_Weights


class ResnetModel:
  def __init__(self, num_classes: int, pretrained_model: bool) -> None:

    assert isinstance(num_classes, int)
    assert isinstance(pretrained_model, bool)
    
    self.num_classes = num_classes
    self.pretrained_model = pretrained_model
  
    if self.pretrained_model:
      self.model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)
    else:
      self.model = resnet50(weights=None)
 
    self.criterion = torch.nn.CrossEntropyLoss()
    self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)



if __name__=="__main__":
  try:
    model = ResnetModel(num_classes=10, pretrained_model=True)
    print("Model was successfully created")
  except ValueError:
    print("Model could not be created")