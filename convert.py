import trimesh
import os
import time
from concurrent.futures import ProcessPoolExecutor

def convert_to_stl(input_file, output_file):
    # Load the mesh
    mesh = trimesh.load(input_file)
    
    # Export the mesh to STL format
    mesh.export(output_file)
    print(f"Converted {input_file} to {output_file}")

def process_file(file_name, input_directory, output_directory):
    if file_name.endswith('.obj') or file_name.endswith('.ply'):
        input_path = os.path.join(input_directory, file_name)
        output_path = os.path.join(output_directory, f"{os.path.splitext(file_name)[0]}.stl")
        convert_to_stl(input_path, output_path)

def main():
    # Define your input and output directories
    input_directory = './Meshes'
    output_directory = './Meshes/Final'

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Get list of files to process
    files_to_process = [
        file_name for file_name in os.listdir(input_directory)
        if file_name.endswith('.obj') or file_name.endswith('.ply')
    ]

    start_time = time.time()
    print(f"Beginning mesh conversions (Current time: {time.strftime('%H:%M:%S', time.localtime(start_time))})")

    # Create a process pool executor
    with ProcessPoolExecutor() as executor:
        # Submit tasks for each file in the input directory
        futures = [
            executor.submit(process_file, file_name, input_directory, output_directory)
            for file_name in files_to_process
        ]

        # Wait for all futures to complete
        for future in futures:
            future.result()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Completed mesh conversions, took {elapsed_time:.2f} seconds (Finished at: {time.strftime('%H:%M:%S', time.localtime(end_time))})")

if __name__ == "__main__":
    main()
