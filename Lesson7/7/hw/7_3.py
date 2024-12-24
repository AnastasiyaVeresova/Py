import generate_name_file, generate_number_file, process_files, rename_files, sort_files
from sort_files import generate_with_dictionary

if __name__ == '__main__':
    generate_name_file.generate_name_file('data_names.txt', 15)
    generate_number_file.generate_number_file(10, 'data.txt')
    process_files.process_files('data.txt', 'data_names.txt', 'f_res.txt')
    rename_files.rename_files(
        desired_name="_new_name",
        num_digits=3,
        src_extension="txt",
        dest_extension="txt",
        name_range=[0, 4],
        directory="./"
    )
    d = {
        'doc': 2,
        'jpg': 1,
        'png': 3
    }
    generate_with_dictionary(d)
    sort_files.sort_files('files')
