from torch.nn import Module, Conv2d, Linear, MaxPool2d, ReLU, Softmax
import torch

class PolicyNetwork(Module):
  '''
  Neural Network with one hidden layer with the state being the input of the network 
  and the ouput being the probability of taking possible individual actions.
  '''
  def __init__(self, n_state, n_action, n_hidden, lr):
      super(PolicyNetwork, self).__init__()

      # initialize first set of CONV => RELU => POOL layers
      self.conv1 = Conv2d(in_channels= 3, out_channels= n_hidden,
        kernel_size=(3, 3))
      self.relu1 = ReLU()
      self.maxpool1 = MaxPool2d(kernel_size=(2, 2), stride=(2, 2))

      # initialize second set of CONV => RELU => POOL layers
      self.conv2 = Conv2d(in_channels=n_hidden, out_channels=256,
        kernel_size=(5, 5))
      self.relu2 = ReLU()
      self.maxpool2 = MaxPool2d(kernel_size=(2, 2), stride=(2, 2))

      # initialize first (and only) set of FC => RELU layers
      self.fc1 = Linear(in_features=9216, out_features=500)
      self.relu3 = ReLU()

      # initialize our softmax classifier
      self.fc2 = Linear(in_features=500, out_features= n_action)
      self.Softmax = Softmax(dim=-1)

      self.optimizer = torch.optim.Adam(self.parameters(), lr)

  def forward(self, x):
    '''
    x = action probability
    '''
    x = self.maxpool1(self.relu1(self.conv1(x)))
    x = self.maxpool2(self.relu2(self.conv2(x)))
    x = self.relu3(self.fc1(torch.flatten(x)))
    print(x.shape)
    x = self.Softmax(self.fc2(x)) 
    return x
  
  def get_action(self, s):
    """
    Estimate the policy and sample an action, compute its log probability
    @param s: input state permutated for animal AI 
    @return: the selected action and log probability
    """
    reshape_s = torch.reshape(torch.Tensor(s), (1, 3, 36, 36))
    logits = self.forward(reshape_s) # probability distribution
    dist = torch.distributions.Categorical(logits=logits)
    action = dist.sample()
    # entropy = dist.entropy().unsqueeze(-1)
    # is_exploratory = None action != np.argmax(logits.detach().numpy())
    return action.item()

  def get_action_alt(self, s):
    """
    Estimate the policy and sample an action, compute its log probability
    @param s: input state permutated for animal AI 
    @return: the selected action and log probability
    """
    reshape_s = torch.reshape(torch.Tensor(s), (1, 3, 36, 36))
    probs = self.forward(reshape_s) # probability distribution
    action = torch.multinomial(probs, 1).item() # rather than np.random.choice(n_actions, p=np.squeeze(probs.detach().numpy()))
    return action

  def update(self, returns, log_probs):
      """
      Update the weights of the policy network given the training samples
      @param returns: return (cumulative rewards) for each step in an episode
      @param log_probs: log probability for each step
      """
      policy_gradient = []

      # given data in an episode (including the returns and the log probability of all steps, 
      # compute gradients for backpropagation
      for log_prob, Gt in zip(log_probs, returns):
          policy_gradient.append(-log_prob * Gt) # gradient terms, negative for maximizing

      loss = torch.stack(policy_gradient).sum()
      self.optimizer.zero_grad()
      loss.backward() # update via backpropagation
      self.optimizer.step()