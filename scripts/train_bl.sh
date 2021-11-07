#!/bin/sh
env="BoxLocking"
scenario_name="empty"
num_agents=2
num_boxes=2
floor_size=12.0
grid_size=60
task_type='all-return'
# algo='bl_actor_critic_eval100_epsilon4'
algo="check"
seed=1

CUDA_VISIBLE_DEVICES=2 python train_bl.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario_name} --num_agents ${num_agents} --num_boxes ${num_boxes} --task_type ${task_type} --seed ${seed} --floor_size ${floor_size} --grid_size ${grid_size}  --n_rollout_threads 3 --episode_length 60 --env_horizon 60 --num_mini_batch 1  --num_env_steps 200000000 --ppo_epoch 15 --attn --save_interval 50 --eval --data_chunk_length 40 \
--buffer_length 2000 --epsilon 4 --delta 4 --sol_prop 0.05 --B_exp 200 --h 1 --archive_initial_length 500 --eval_number 3 
# --use_wandb