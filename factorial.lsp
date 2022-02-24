;;; 1. Write a  lambda function in LISP to find factorial for a number. 

(defun factorial (n)
    (cond
        ((= n 0) 1) 
        ((= n 1) 1) 
        (t
            (* n (factorial (- n 1)))
        )
    )
)

(write ((lambda (val) (factorial val)) 5))
