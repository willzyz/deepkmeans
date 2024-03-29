class PTBConfig:
  dataset="ptb"
  data_path="./data/%s" % dataset
  eos_token="eos"
  sos_token="sos"
  checkpoint_dir="checkpoint"
  task="word_prediction"
  decay_rate=0.3
  decay_step=10000
  n_topics=50
  learning_rate=0.00099 
  n_stops=449
  vocab_size=10000 
  n_hidden=300
  n_layers=1
  projector_embed_dim=200
  generator_embed_dim=n_hidden
  dropout=1.0
  max_grad_norm=1.0
  total_epoch=3
  init_scale=0.075
  num_sent=10
  forward_only=True
  print_topics=True
  generate_text=True

class IMDBConfig:
  dataset="imdb"
  data_path = "./data/%s" % dataset
  eos_token="eos"
  unk_token="unk"
  checkpoint_dir="checkpoint_imdb"
  task="sentiment_analysis"
  decay_rate=0.95 
  decay_step=10000
  projector_embed_dim=500
  generator_embed_dim=200
  dropout=1.0
  n_topics=200
  learning_rate=0.004
  n_stops=446
  vocab_size=5000 #including eos and unk
  n_hidden=300
  n_layers=2
  max_grad_norm = 1.0
  total_epoch=20
  init_scale=0.075
  forward_only=False
  print_topics=True
  generate_text=True
  cell_type = 'lstm'




