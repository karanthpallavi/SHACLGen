from linkml.generators.shaclgen import ShaclGenerator
import subprocess

def generate_shacl_with_options(schema_path: str, output_shacl_path: str):
    """
    Generates a SHACL file from a LinkML YAML schema with specific options via the CLI.

    Args:
        schema_path (str): Path to the LinkML YAML schema file.
        output_shacl_path (str): Path to save the generated SHACL file.

    CLI Options:
        --non-closed: Generate shapes that allow open-world data.
        --include-annotations: Include annotations in the SHACL file.
        --metadata: Include schema-level metadata in the SHACL file.
        --mergeimports: Resolve and merge imports into the main schema.

    Returns:
        None
    """
    # Command to run the SHACL generator with options
    command = [
        "/full/path/to/linkml-gen-shacl",  # Replace with the actual path
        "--non-closed",
        "--include-annotations",
        "--metadata",
        "--mergeimports",
        "-o", output_shacl_path,
        schema_path
    ]


    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"SHACL file generated with options and saved to {output_shacl_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating SHACL file: {e}")
    except FileNotFoundError:
        print("Error: linkml-gen-shacl command not found. Ensure LinkML is installed and accessible.")

def generate_shacl_from_linkml(schema_path: str, output_shacl_path: str):
    """
    Generates a SHACL file from a LinkML YAML schema with focus nodes for validation.

    Args:
        schema_path (str): Path to the LinkML YAML schema file.
        output_shacl_path (str): Path to save the generated SHACL file.

    Returns:
        None
    """
    # Generate SHACL from the schema file
    shacl_generator = ShaclGenerator(schema_path)
    shacl_content = shacl_generator.serialize()

    # Write the SHACL content to a file
    with open(output_shacl_path, "w") as shacl_file:
        shacl_file.write(shacl_content)

    print(f"SHACL file generated and saved to {output_shacl_path}")

# Example usage:
# Replace these paths with your actual file paths
linkml_schema_path = "Measurement/ScalarMeasurementDatum.yaml"
shacl_output_path = "OutputShacl/Measurement/ScalarMeasurementDatum_22JanWithOptions.shacl.ttl"
#generate_shacl_from_linkml(linkml_schema_path, shacl_output_path)
generate_shacl_with_options(linkml_schema_path, shacl_output_path)