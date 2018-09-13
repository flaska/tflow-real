import data
import model
import history
import vis

from tensorflow import keras

(train_data, train_labels), (test_data, test_labels) = data.get_data()

model = model.build_model(train_data)
model.summary()

EPOCHS = 500


class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

history_results = model.fit(train_data, train_labels, epochs=EPOCHS,
                    validation_split=0.2, verbose=0,
                    callbacks=[PrintDot()])

# early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=20)
# history_results = model.fit(train_data, train_labels, epochs=EPOCHS,
#                     validation_split=0.2, verbose=0,
#                     callbacks=[early_stop, PrintDot()])

[loss, mae] = model.evaluate(test_data, test_labels, verbose=0)

print("Testing set Mean Abs Error: ${:7.2f}".format(mae))

history.plot_history(history_results)

x = model.predict(test_data)
test_predictions = x.flatten()

vis.display(test_labels, test_predictions)