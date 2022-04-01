package ink.organics.demo;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DemoController {


    @PostMapping("/sss")
    public ResponseEntity sss(DemoDTO dto) {
        return ResponseEntity.ok(dto);
    }
}
