from torch.utils.data import Dataset


class Memory(Dataset):
    def __init__(self, states, *args) -> None:
        super().__init__()

        self.states = states
        self.data = args

    def __len__(self):
        return len(self.states)

    def __getitem__(self, idx):
        # return states and each additional data in args at the same index
        return self.states[idx], *[data[idx] for data in self.data]



