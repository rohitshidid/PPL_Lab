;;; 2. Write a user defined function to find nth element from a list using LISP. (Use car and cdr functions)

(defun findN (n listVal)
    (if (zerop n)
        (car listVal)
    (findN (1- n) (cdr listVal)))
)
 
(write (findN 0 (list 1 2 3)))
