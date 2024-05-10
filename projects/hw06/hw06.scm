;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (unique s)
  (if (null? s)
      nil
      (cons (car s) (unique (filter (lambda (e) (not (equal? e (car s)))) (cdr s))))
  )
)


(define (cons-all first rests)
    (map (lambda (x) (cons first x)) rests)
)

;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  'YOUR-CODE-HERE
  )

; Tail recursion

(define (replicate x n)
  'YOUR-CODE-HERE
  )

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
)

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
)


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
)