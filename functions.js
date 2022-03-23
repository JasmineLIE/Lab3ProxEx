const content = 0;

function countMarsh() {
    content += 1;
}

FileSystem.writeFile('marshmellow.txt', content)