#!/bin/sh
ulimit -n 4096 
env="MPE"
scenario="push_ball"
num_landmarks=2
num_agents=2
num_boxes=2
algo='phase_warmup6iter_pb'
# algo='check'
seed_max=1

echo "env is ${env}, scenario is ${scenario}, algo is ${algo}, seed is ${seed_max}"

# for seed in `seq ${seed_max}`;
# do
#     echo "seed is ${seed}:"
#     CUDA_VISIBLE_DEVICES=1 python train_mpe_curriculum_pb_stage.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario} --num_agents ${num_agents} --num_landmarks ${num_landmarks} --num_boxes ${num_boxes}  --seed ${seed} --n_rollout_threads 500 --num_mini_batch 1 --episode_length 120 --num_env_steps 600000000 --ppo_epoch 15 --recurrent_policy --use_popart
#     echo "training is done!"
# done
seed=3
CUDA_VISIBLE_DEVICES=2 python train_mpe_curriculum_pb_stage.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario} --num_agents ${num_agents} --num_landmarks ${num_landmarks} --num_boxes ${num_boxes}  --seed ${seed} --n_rollout_threads 500 --num_mini_batch 16 --episode_length 120 --num_env_steps 600000000 --ppo_epoch 15 --recurrent_policy --use_popart
