#!/bin/bash

rm -rf /tmp/sidBox
mkdir /tmp/sidBox

echo "Start record and save asr result to /tmp/sidBox/output.wav.txt"
python3 baidu_asr.py

# Function to split text into chunks of at most 1024 bytes
split_text() {
    input_file=$1
    output_prefix=$2
    max_size=1024

    # Split the text into chunks
    csplit --quiet --prefix="$output_prefix" --suffix-format="%03d.txt" "$input_file" "/^$/" "{*}"

    # Merge chunks that are smaller than the max_size
    for file in ${output_prefix}*; do
        size=$(wc -c <"$file")
        if [ $size -le $max_size ]; then
            cat "$file" >> "${file%.*}.merged.txt"
            rm "$file"
        fi
    done
}

echo "======chat with chatgpt====="
echo "sgpt "$(cat /tmp/sidBox/output.wav.txt)""
source ../_install/chatgpt_cli/bin/activate

# Run chatgpt and save the response to a temporary file
sgpt "$(cat /tmp/sidBox/output.wav.txt)(回复少于1024字节且不加换行)" | tee /tmp/sidBox/response.txt

# 使用sed命令来删除文本中的换行符
# sed ':a;N;$!ba;s/\n//g' /tmp/sidBox/response.txt > /tmp/sidBox/new_response.txt

# Split the response text into chunks
split_text "/tmp/sidBox/response.txt" "/tmp/sidBox/response_chunk"

# Start TTS for each chunk and play the sound
for file in /tmp/sidBox/response_chunk*.merged.txt; do
    echo "Start TTS for $file"
    python3 baidu_tts.py "$file" "${file%.*}.wav"
    echo "Play the sound for $file"
    paplay "${file%.*}.wav" --no-remap
done

echo "Done"
