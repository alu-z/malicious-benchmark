import java.io.IOException;

class SafeProcessBuilder {
    public void runGitStatus() throws IOException {
        new ProcessBuilder("git", "status").start();
    }
}

