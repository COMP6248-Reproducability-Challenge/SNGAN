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

###If need use the BN_DCGAN OR LN_DCGAN code

you should download the inception score module fokred from: [chainer-inception-score](https://github.com/hvy/chainer-inception-score)

and download the inception model.
```
cd common/inception
python download.py --outfile inception_score.model
```
You can start training with ```train.py```.
```
train.py --gpu 0 --algorithm dcgan --batchsize 64 --out drive/res --adam_alpha 0.0002 --adam_beta1 0.5 --adam_beta2 0.9
```
