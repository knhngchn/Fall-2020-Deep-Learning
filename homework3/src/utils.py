import numpy as np


def lr_schedule(cur_epoch, cur_lr):
    new_lr = cur_lr * 1 / (1 + 0.001 * cur_epoch)

    return new_lr

def CEloss(probs, labels):
    """cross entropy loss function
    Args:
        probs: The predicted probabilities of each class.
        labels: The corresponding ground truth.

    Return:
        CE_loss: The output CE loss.
    """
    
    B = probs.shape[0]
    one_hot_encoded_labels = one_hot_encoding(labels)
    log_sum = np.sum(np.multiply(one_hot_encoded_labels, np.log(probs)))
    CE_loss = - (1. / B) * log_sum

    return CE_loss

def one_hot_encoding(labels, num_class=3):
    """convert labels to one hot encoded version
    """
    
    B = len(labels)
    output = np.zeros((B, num_class), dtype=int)
    for i in range(B):
        output[i][int(labels[i])] = 1

    return output

def print_confusion_matrix(confusion_matrix_data):

    message = ''
    message += '  Predicted   0   1   2   All\n'
    message += '  Actual\n'
    message += '    0         {:3d} {:3d} {:3d} {:3d}\n'.format(*confusion_matrix_data['actual_0'], sum(confusion_matrix_data['actual_0']))
    message += '    1         {:3d} {:3d} {:3d} {:3d}\n'.format(*confusion_matrix_data['actual_1'], sum(confusion_matrix_data['actual_1']))
    message += '    2         {:3d} {:3d} {:3d} {:3d}\n'.format(*confusion_matrix_data['actual_2'], sum(confusion_matrix_data['actual_2']))
    predicteds = [0, 0, 0]
    for predicted_list in confusion_matrix_data.values():
        for i, predicted in enumerate(predicted_list):
            predicteds[i] += predicted
    message += '   All        {:3d} {:3d} {:3d} {:3d}'.format(*predicteds, sum(predicteds))

    return message
