import torch
from torchvision.utils import make_grid

from src.callbacks.loggers.base_logger import BaseLogger


class AcdcSISRLogger(BaseLogger):
    """The ACDC logger for the Single-Image Super-Resolution.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _add_images(self, epoch, train_batch, train_output, valid_batch, valid_output):
        """Plot the visualization results.
        Args:
            epoch (int): The number of trained epochs.
            train_batch (dict): The training batch.
            train_output (torch.Tensor): The training output.
            valid_batch (dict): The validation batch.
            valid_output (torch.Tensor): The validation output.
        """
        train_hr_img = make_grid(train_batch['hr_img'], nrow=1, normalize=True, scale_each=True, pad_value=1)
        train_sr_img = make_grid(train_output, nrow=1, normalize=True, scale_each=True, pad_value=1)
        valid_hr_img = make_grid(valid_batch['hr_img'], nrow=1, normalize=True, scale_each=True, pad_value=1)
        valid_sr_img = make_grid(valid_output, nrow=1, normalize=True, scale_each=True, pad_value=1)

        train_grid = torch.cat([train_hr_img, train_sr_img], dim=-1)
        valid_grid = torch.cat([valid_hr_img, valid_sr_img], dim=-1)
        self.writer.add_image('train', train_grid)
        self.writer.add_image('valid', valid_grid)
