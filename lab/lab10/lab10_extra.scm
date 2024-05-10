;; Scheme ;;


(define lst
  (list '(1) 2 '(3 4) 5)

)

(define (composed f g)
    (define (composing x)
      (define medium (g x))
      (f medium))
  composing
)

(define (remove item lst)
  (if (null? lst)
    '()
    (if (= item (car lst))
      (remove item (cdr lst))
      (cons (car lst) (remove item (cdr lst)))
    )
  )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (in-list s x)
    (if (null? s)
      #f
      (if (= (car s) x)
        #t
        (in-list (cdr s) x)
      )
    )
)
(define (no-repeats s)
  (if (null? s)
    nil
    (if (in-list (cdr s) (car s))
      (no-repeats (cdr s))
      (cons (car s) (no-repeats (cdr s)))
    )
  )
)

(define (substitute s old new)
  (if (null? s)
    nil
    (if (pair? (car s))
      (cons (substitute (car s) old new) (substitute (cdr s) old new))
      (if (equal? (car s) old)
        (cons new (substitute (cdr s) old new))
        (cons (car s) (substitute (cdr s) old new))
      )

    )
  )
)


(define (sub-all s olds news)
  (if (null? olds)
    s
    (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
  )
)
