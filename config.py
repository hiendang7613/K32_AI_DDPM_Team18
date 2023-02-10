
"""## Hyperparameters"""

dataset_cfg = {
    'dataset_name' : "celeb_a:2.0.1",
    'splits' : ["train"],
    'data_dir':'./celeb_a/content',
    'num_train_records': 162770,
    'img_shape': (32,32,3), 
    'clip_min' : -1.0,
    'clip_max' : 1.0,
}

train_cfg = {
    'batch_size': 64,
    'num_epochs' : 800,
    'learning_rate' : 2e-4
}

model_cfg = {
    'norm_groups' : 8,
    'total_timesteps' : 1000,
    'first_conv_channels' : 128,
    'channel_multiplier' : [1, 2, 2, 2],
    'has_attention' : [False, False, False, True],
    'num_res_blocks' : 2 ,
}
model_cfg['widths'] = [model_cfg['first_conv_channels'] * mult for mult in model_cfg['channel_multiplier']]






