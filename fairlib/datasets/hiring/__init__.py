from .hiring import hiring

def init_data_class(dest_folder, batch_size):
    return hiring(dest_folder = dest_folder, batch_size=batch_size)
