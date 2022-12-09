model = Net().to(device)
optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)

def train(log_interval, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval ==0:
            print('Train Epoch: {} [{}/{} ({:.0f}%')\tloss: {:.6f}.format(
                epoch, batch_idx *len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item())
            )