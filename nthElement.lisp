(defun nth2 (n lst)
  (if (zerop n)
    (car lst)
    (nth2 (1- n) (cdr lst))))
    
(let ((x (read)))
(write(nth2 x (list 10 20 30 40 50 60 70 80 90 100))))


