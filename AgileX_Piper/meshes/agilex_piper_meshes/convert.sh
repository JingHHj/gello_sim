 #!/bin/bash

# Iterate over all .dae files and convert them to .stl using MeshLab
for file in *.dae; do
    if [[ -f "$file" ]]; then
        base_name="${file%.dae}"
        meshlabserver -i "$file" -o "${base_name}.STL"
    fi
done

