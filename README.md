# Mesh Conversion Project

This project converts `.ply` and `.obj` mesh files to `.stl` format. Follow the steps below to set up and run the conversion process.

## Instructions

1. **Place Mesh Files**

   - Place all your `.ply` and `.obj` mesh files inside the `Meshes` folder.

2. **Create Python Virtual Environment**

   - Run the following command to create a virtual environment:
     ```sh
     python -m venv venv
     ```

3. **Activate Virtual Environment**

   - Activate the virtual environment with the following command:
     - On Windows:
       ```sh
       .\venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```sh
       source venv/bin/activate
       ```

4. **Install Dependencies**

   - Install the required dependencies from the `requirements.txt` file:
     ```sh
     pip install -r requirements.txt
     ```

5. **Run Conversion Script**

   - Execute the conversion script:
     ```sh
     python .\convert.py
     ```

6. **Locate Converted Files**
   - Find all the converted `.stl` files inside the `Meshes/Final/` directory.
