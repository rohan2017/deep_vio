import os

class Parameters():
	def __init__(self):
		self.n_processors = 16
		# Path
		self.image_dir = '/nfs/nas12.ethz.ch/fs1201/infk_ivc_students/cvg-students/chsiao/KITTI/images/'
		self.pose_dir = '/nfs/nas12.ethz.ch/fs1201/infk_ivc_students/cvg-students/chsiao/KITTI/pose_GT/'


		self.train_video = ['00', '02', '08', '09', '01', '06', ] 
		self.valid_video = ['04', '05', '07', '10']
		self.partition = None  # partition videos in 'train_video' to train / valid dataset


		# Data Preprocessing
		self.resize_mode = 'rescale' # 'crop' 'rescale' None
		self.img_w = 608   #  1226
		self.img_h = 184   #  370
		self.img_means = (-0.14968217427134656, -0.12941663107068363, -0.1320610301921484) 
		self.img_stds = (1, 1, 1)  #(0.309122, 0.315710, 0.3226514)
		self.minus_point_5 = True

		self.seq_len = (4, 6)  # [7, 9]
		self.sample_times = 3  # 1

		# Data info path
		self.train_data_info_path = 'datainfo/train_df_t{}_v{}_p{}_seq{}x{}_sample{}.pickle'.format(''.join(self.train_video), ''.join(self.valid_video), self.partition, self.seq_len[0], self.seq_len[1], self.sample_times)
		self.valid_data_info_path = 'datainfo/valid_df_t{}_v{}_p{}_seq{}x{}_sample{}.pickle'.format(''.join(self.train_video), ''.join(self.valid_video), self.partition, self.seq_len[0], self.seq_len[1], self.sample_times)


		# Model
		self.rnn_hidden_size = 1000
		self.conv_dropout = (0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1)
		self.rnn_dropout_in = 0.5
		self.rnn_dropout_out = 0.5
		self.rnn_dropout_between = 0.5  # 0: no dropout
		self.clip = None # 5
		self.batch_norm = True
		# Training
		self.batch_size = 16
		self.pin_mem = True
		self.epochs = 100
		self.optim = {'opt': 'Adagrad', 'lr': 0.001}
					# {'opt': 'Adagrad', 'lr': 0.001}
					# {'opt': 'Adam'}
					# {'opt': 'Cosine', 'T': 100 , 'lr': 0.001}
		
		# Pretrain, Retrain
		self.pretrained_flownet = None
								# './pretrained/flownets_bn_EPE2.459.pth.tar'  
								# './pretrained/flownets_EPE1.951.pth.tar'
		self.resume = False
		self.resume_t_or_v = '.train'
		self.load_model_path = 'models/t{}_v{}_im{}x{}_s{}x{}_b{}_rnn{}_{}.model{}'.format(''.join(self.train_video), ''.join(self.valid_video), self.img_h, self.img_w, self.seq_len[0], self.seq_len[1], self.batch_size, self.rnn_hidden_size, '_'.join([k+str(v) for k, v in self.optim.items()]), self.resume_t_or_v)
		self.load_optimizer_path = 'models/t{}_v{}_im{}x{}_s{}x{}_b{}_rnn{}_{}.optimizer{}'.format(''.join(self.train_video), ''.join(self.valid_video), self.img_h, self.img_w, self.seq_len[0], self.seq_len[1], self.batch_size, self.rnn_hidden_size, '_'.join([k+str(v) for k, v in self.optim.items()]), self.resume_t_or_v)

		self.record_path = 'records/t{}_v{}_im{}x{}_s{}x{}_b{}_rnn{}_{}.txt'.format(''.join(self.train_video), ''.join(self.valid_video), self.img_h, self.img_w, self.seq_len[0], self.seq_len[1], self.batch_size, self.rnn_hidden_size, '_'.join([k+str(v) for k, v in self.optim.items()]))
		self.save_model_path = 'models/t{}_v{}_im{}x{}_s{}x{}_b{}_rnn{}_{}.model'.format(''.join(self.train_video), ''.join(self.valid_video), self.img_h, self.img_w, self.seq_len[0], self.seq_len[1], self.batch_size, self.rnn_hidden_size, '_'.join([k+str(v) for k, v in self.optim.items()]))
		self.save_optimzer_path = 'models/t{}_v{}_im{}x{}_s{}x{}_b{}_rnn{}_{}.optimizer'.format(''.join(self.train_video), ''.join(self.valid_video), self.img_h, self.img_w, self.seq_len[0], self.seq_len[1], self.batch_size, self.rnn_hidden_size, '_'.join([k+str(v) for k, v in self.optim.items()]))
		
		if not os.path.isdir(os.path.dirname(self.record_path)):
			os.makedirs(os.path.dirname(self.record_path))
		if not os.path.isdir(os.path.dirname(self.save_model_path)):
			os.makedirs(os.path.dirname(self.save_model_path))
		if not os.path.isdir(os.path.dirname(self.save_optimzer_path)):
			os.makedirs(os.path.dirname(self.save_optimzer_path))
		if not os.path.isdir(os.path.dirname(self.train_data_info_path)):
			os.makedirs(os.path.dirname(self.train_data_info_path))

par = Parameters()

