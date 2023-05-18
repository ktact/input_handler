#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

int main() {
    const char *fifo_path = "/tmp/my_pipe";

    // Sample mouse events
    const char *mouse_events[] = {
        "{ \"x\": 100, \"y\": 100 }\n",
        "{ \"x\": 500, \"y\": 500 }\n"
    };
    int num_events = sizeof(mouse_events) / sizeof(mouse_events[0]);

    // Open the named pipe for writing
    int fd = open(fifo_path, O_WRONLY);
    if (fd == -1) {
        perror("open");
        return 1;
    }

    // Write the mouse events to the named pipe
    for (int i = 0; i < num_events; i++) {
        write(fd, mouse_events[i], strlen(mouse_events[i]));
        sleep(1); // Add a delay between events
    }

    // Close the named pipe
    close(fd);

    return 0;
}
