#!/bin/sh
ulimit -n 4096 
env="MPE"
scenario="simple_speaker_listener"
num_landmarks=3
num_agents=2
algo="sl_reverse"
# algo='check'
seed=1

echo "env is ${env}, scenario is ${scenario}, algo is ${algo}, seed is ${seed}"

CUDA_VISIBLE_DEVICES=0 python sl_reverse.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario} --num_agents ${num_agents} --num_landmarks ${num_landmarks} --seed ${seed} --n_rollout_threads 500 --num_mini_batch 2 --episode_length 70 --num_env_steps 100000000 --ppo_epoch 15 --recurrent_policy --share_policy