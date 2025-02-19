 #!/bin/bash

# Iterate over all .dae files in the current directory
for file in *.dae; do
    # Check if the file exists to avoid issues if no .dae files are present
    if [[ -f "$file" ]]; then
        # Extract the filename without the extension
        base_name="${file%.dae}"
        # Rename the file
        mv "$file" "${base_name}_collision.dae"
    fi
done

