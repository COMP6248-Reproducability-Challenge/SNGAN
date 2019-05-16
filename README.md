# SPECTRAL NORMALIZATION FOR GENERATIVE ADVERSARIAL NETWORKS

This repository is mainly for reproduce a paper : [SPECTRAL NORMALIZATION FOR GENERATIVE ADVERSARIAL NETWORKS](https://arxiv.org/abs/1802.05957)<br>

We compare the difference between SNGAN and some other versions of gan, such as WGAN-GP,BEGAN,EBGAN and DCGAN based on BN and LN.<br>

These codes are evaluated with the inception score and Fréchet Inception Distance on Cifar-10 dataset.<br>

The implementation of WGAN-GP, BEGAN and EBGAN is based on:[pytorch-generative-model-collections](https://github.com/znxlwm/pytorch-generative-model-collections)

The implementation of DCGAN using BN and LN is based on: [chainer-gan-lib](https://github.com/pfnet-research/chainer-gan-lib)

The implementation of FID score is based on: [pytorch-fid](https://github.com/mseitzer/pytorch-fid)

The implementation of the Inception score is based on: [inception-score-pytorch](https://github.com/sbarratt/inception-score-pytorch)

SNGAN's code is implemented by ourselves.
## How to use

Install the requirements first:
```
pip install -r requirements.txt
```
