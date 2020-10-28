import matplotlib.pyplot as plt
import json
import pdb
import numpy as np
import os
import csv

def main():
    scenario = 'simple_spread'
    save_dir = './' + scenario + '/'
    save_name = 'sp_tricks'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # solved_sp
    exp_name = 'solved_sp'
    data_dir =  './' + exp_name + '.csv'
    x_step = []
    y_seed = []
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step.append(row[0])
            y_seed.append(row[1:])
    x_step = x_step[1:]
    y_seed = y_seed[1:]
    for i in range(len(x_step)):
        x_step[i] = np.float(x_step[i])
        for j in range(len(y_seed[i])):
            y_seed[i][j] = np.float(y_seed[i][j])
    x_step = np.array(x_step)
    y_seed = np.array(y_seed)
    mean_seed = np.mean(y_seed,axis=1)
    std_seed = np.std(y_seed,axis=1)
    plt.plot(x_step,mean_seed,label=exp_name)
    plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # diversified_sp
    exp_name = 'diversified_sp'
    data_dir =  './' + exp_name + '.csv'
    x_step = []
    y_seed = []
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step.append(row[0])
            y_seed.append(row[1:])
    x_step = x_step[1:]
    y_seed = y_seed[1:]
    for i in range(len(x_step)):
        x_step[i] = np.float(x_step[i])
        for j in range(len(y_seed[i])):
            y_seed[i][j] = np.float(y_seed[i][j])
    x_step = np.array(x_step)
    y_seed = np.array(y_seed)
    mean_seed = np.mean(y_seed,axis=1)
    std_seed = np.std(y_seed,axis=1)
    plt.plot(x_step,mean_seed,label=exp_name)
    plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # diversified_novelty_sp
    exp_name = 'diversified_novelty_sp'
    data_dir =  './' + exp_name + '.csv'
    x_step = []
    y_seed = []
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step.append(row[0])
            y_seed.append(row[1:])
    x_step = x_step[1:]
    y_seed = y_seed[1:]
    for i in range(len(x_step)):
        x_step[i] = np.float(x_step[i])
        for j in range(len(y_seed[i])):
            y_seed[i][j] = np.float(y_seed[i][j])
    x_step = np.array(x_step)
    y_seed = np.array(y_seed)
    mean_seed = np.mean(y_seed,axis=1)
    std_seed = np.std(y_seed,axis=1)
    plt.plot(x_step,mean_seed,label=exp_name)
    plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # diversified_novelty_parentsampling_sp
    exp_name = 'diversified_novelty_parentsampling_sp'
    data_dir =  './' + exp_name + '.csv'
    x_step = []
    y_seed = []
    with open(data_dir,'r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            x_step.append(row[0])
            y_seed.append(row[1:])
    x_step = x_step[1:]
    y_seed = y_seed[1:]
    for i in range(len(x_step)):
        x_step[i] = np.float(x_step[i])
        for j in range(len(y_seed[i])):
            y_seed[i][j] = np.float(y_seed[i][j])
    x_step = np.array(x_step)
    y_seed = np.array(y_seed)
    mean_seed = np.mean(y_seed,axis=1)
    std_seed = np.std(y_seed,axis=1)
    plt.plot(x_step,mean_seed,label=exp_name)
    plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    plt.xlabel('timesteps')
    plt.ylabel('coverage rate')
    plt.legend()
    plt.savefig(save_dir + save_name + '.jpg')


    # scenario = 'push_ball'
    # save_dir = './' + scenario + '/'
    # save_name = 'pb_tricks'
    # if not os.path.exists(save_dir):
    #     os.makedirs(save_dir)

    # # solved_sp
    # exp_name = 'solved_pb'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label=exp_name)
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # # diversified_sp
    # exp_name = 'diversified_pb'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label=exp_name)
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # # diversified_novelty_sp
    # exp_name = 'diversified_novelty_pb'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label=exp_name)
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # # diversified_novelty_parentsampling_sp
    # exp_name = 'diversified_novelty_parentsampling_pb'
    # data_dir =  './' + exp_name + '.csv'
    # x_step = []
    # y_seed = []
    # with open(data_dir,'r') as csvfile:
    #     plots = csv.reader(csvfile)
    #     for row in plots:
    #         x_step.append(row[0])
    #         y_seed.append(row[1:])
    # x_step = x_step[1:]
    # y_seed = y_seed[1:]
    # for i in range(len(x_step)):
    #     x_step[i] = np.float(x_step[i])
    #     for j in range(len(y_seed[i])):
    #         y_seed[i][j] = np.float(y_seed[i][j])
    # x_step = np.array(x_step)
    # y_seed = np.array(y_seed)
    # mean_seed = np.mean(y_seed,axis=1)
    # std_seed = np.std(y_seed,axis=1)
    # plt.plot(x_step,mean_seed,label=exp_name)
    # plt.fill_between(x_step,mean_seed-std_seed,mean_seed+std_seed,alpha=0.1)

    # plt.xlabel('timesteps')
    # plt.ylabel('coverage rate')
    # plt.legend()
    # plt.savefig(save_dir + save_name + '.jpg')

if __name__ == "__main__":
    main()