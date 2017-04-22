import os

#Each website has a seperate project folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.mkdir(directory)

# Create queue and a list for crawled files
def create_data_file(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# Add data to existing file
def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data  + '\n')

# Empty the file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

# Read the links from file to a set
def file_to_set(filename):
    results = set()
    with open(filename, 'r') as f:
        for line in f:
            results.add(line.rstrip())
    return results

# Add each link in the set to our file
def set_to_file(links, filename):
    delete_file_contents(filename)
    for link in sorted(links):
        append_to_file(filename, link)

# create_project_dir('thenewboston')
# create_data_file('thenewboston', 'thenewboston.com')