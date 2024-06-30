tp = input("tp = ")
fp = input("fp = ")
fn = input("fn = ")
if not tp.lstrip('-').isdigit():
    print('tp must be int')
elif not fp.lstrip('-').isdigit():
    print('fp must be int')
elif not fn.lstrip('-').isdigit():
    print('fn must be int')
else:
  tp = int(tp)
  fp = int(fp)
  fn = int(fn)
  if tp <= 0 or fp <= 0 or fn <= 0:
    print('tp and fp and fn must be greater than zero')
  else:
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    # In kết quả
    print(f'Precision is {precision}')
    print(f'Recall is {recall}')
    print(f'F1-Score is {f1_score}')