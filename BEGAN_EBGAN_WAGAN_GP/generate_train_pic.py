import utils
from dataloader import dataloader

data_loader = dataloader('cifar10', 28, 64)
data = data_loader.__iter__().__next__()[0]
print(data.shape)
samples = data.data.numpy().transpose(0, 2, 3, 1)
image_frame_dim = 8
samples = (samples + 1) / 2
utils.save_images(samples[:image_frame_dim * image_frame_dim, :, :, :], [image_frame_dim, image_frame_dim]
                  ,  # image_frame_dim * image_frame_dim
                 'train_pic/'+'1'+'.png')