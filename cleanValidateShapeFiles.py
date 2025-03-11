import os
import chardet

def replace_crlf_with_lf_encoding(input_dir, output_dir):
    """
    Replaces CRLF (\r\n) with LF (\n) in all .ttl files in a directory, handling various encodings.

    Args:
        input_dir (str): Path to the input directory.
        output_dir (str): Path to the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".ttl"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            try:
                # Detect file encoding
                with open(input_path, 'rb') as f:
                    raw_data = f.read()
                    encoding = chardet.detect(raw_data)['encoding']

                # Handle decoding errors
                if encoding is None:
                    print(f"Could not detect encoding for {input_path}. Skipping...")
                    continue

                # Read the file with the detected encoding
                with open(input_path, 'r', encoding=encoding, errors='replace') as f:
                    content = f.read()

                # Replace CRLF with LF
                updated_content = content.replace('\r\n', '\n')

                # Write the updated content back using UTF-8
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                print(f"Processed file: {input_path} -> {output_path}")

            except Exception as e:
                print(f"Error processing file {input_path}: {e}")

# Example usage
input_directory = "shapesFilesInput"  # Replace with your input directory path
output_directory = "shapesFilesOutput"  # Replace with your output directory path
replace_crlf_with_lf_encoding(input_directory,output_directory)


def replace_crlf_in_directory(input_dir, output_dir):
    """
    Replaces CRLF (\r\n) with LF (\n) in all .ttl files in a directory.

    Args:
        input_dir (str): Path to the input directory containing .ttl files.
        output_dir (str): Path to the output directory where processed files will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create output directory if it doesn't exist

    for filename in os.listdir(input_dir):
        if filename.endswith(".ttl"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename)

            try:
                # Read and replace CRLF with LF
                with open(input_file, 'rb') as f:
                    content = f.read()

                updated_content = content.replace(b'\r\n', b'\n')

                # Write to the output file
                with open(output_file, 'wb') as f:
                    f.write(updated_content)

                print(f"Processed file: {input_file} -> {output_file}")
            except Exception as e:
                print(f"Error processing file {input_file}: {e}")

def replace_crlf_binary(input_dir, output_dir):
    """
    Replaces CRLF (\r\n) with LF (\n) in all files as raw binary data.

    Args:
        input_dir (str): Path to the input directory.
        output_dir (str): Path to the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".ttl"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            try:
                with open(input_path, 'rb') as f:
                    content = f.read()

                updated_content = content.replace(b'\r\n', b'\n')

                with open(output_path, 'wb') as f:
                    f.write(updated_content)

                print(f"Processed (binary): {input_path} -> {output_path}")

            except Exception as e:
                print(f"Error processing file {input_path}: {e}")


#replace_crlf_binary(input_directory, output_directory)


#replace_crlf_in_directory(input_directory, output_directory)
