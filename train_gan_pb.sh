#!/bin/sh
ulimit -n 32768
env="MPE"
scenario="push_ball"
num_landmarks=2
num_agents=2
algo="gan_pb_addinitialtasks"
# algo='check'
seed=3

echo "env is ${env}, scenario is ${scenario}, algo is ${algo}, seed is ${seed}"

CUDA_VISIBLE_DEVICES=2 python train_gan_pb.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario} --num_agents ${num_agents} --num_landmarks ${num_landmarks} --seed ${seed} --n_rollout_threads 500 --num_mini_batch 2 --episode_length 120 --num_env_steps 80000000 --ppo_epoch 15 --recurrent_policy --use_popart
