Chắc chắn rồi, đây là bản dịch tiếng Việt của đoạn văn bản bạn đã cung cấp:

# 2.2 Dữ liệu Phân cấp và Tính Chất Đóng

Như chúng ta đã thấy, các cặp cung cấp một "chất kết dính" nguyên thủy mà chúng ta có thể sử dụng để xây dựng các đối tượng dữ liệu phức hợp. [Hình 2.2](#Figure-2_002e2) cho thấy một cách tiêu chuẩn để hình dung một cặp—trong trường hợp này, cặp được tạo bởi `(cons 1 2)`. Trong biểu diễn này, được gọi là *ký hiệu hộp và con trỏ*, mỗi đối tượng được hiển thị như một *con trỏ* đến một hộp. Hộp cho một đối tượng nguyên thủy chứa một biểu diễn của đối tượng. Ví dụ, hộp cho một số chứa một chữ số. Hộp cho một cặp thực sự là một hộp kép, phần bên trái chứa (một con trỏ đến) `car` của cặp và phần bên phải chứa `cdr`.

![](fig/chap2/Fig2.2e.std.svg 261.12x141.96)
**Hình 2.2:** Biểu diễn hộp và con trỏ của `(cons 1 2)`.

Chúng ta đã thấy rằng `cons` có thể được sử dụng để kết hợp không chỉ các số mà cả các cặp. (Bạn đã sử dụng thực tế này, hoặc đáng lẽ phải sử dụng, trong khi thực hiện [Bài tập 2.2](2_002e1.xhtml#Exercise-2_002e2) và [Bài tập 2.3](2_002e1.xhtml#Exercise-2_002e3).) Do đó, các cặp cung cấp một khối xây dựng phổ quát mà từ đó chúng ta có thể xây dựng tất cả các loại cấu trúc dữ liệu. [Hình 2.3](#Figure-2_002e3) cho thấy hai cách sử dụng các cặp để kết hợp các số 1, 2, 3 và 4.

![](fig/chap2/Fig2.3e.std.svg 667.2x340.92)
**Hình 2.3:** Hai cách kết hợp 1, 2, 3 và 4 bằng các cặp.

Khả năng tạo ra các cặp mà các phần tử là các cặp là bản chất tầm quan trọng của cấu trúc danh sách như một công cụ biểu diễn. Chúng ta gọi khả năng này là *tính chất đóng* của `cons`. Nói chung, một phép toán để kết hợp các đối tượng dữ liệu thỏa mãn tính chất đóng nếu các kết quả của việc kết hợp các thứ với phép toán đó có thể tự chúng được kết hợp bằng cùng một phép toán.^[Việc sử dụng từ "đóng" ở đây xuất phát từ đại số trừu tượng, trong đó một tập hợp các phần tử được cho là đóng dưới một phép toán nếu việc áp dụng phép toán cho các phần tử trong tập hợp tạo ra một phần tử mà lại là một phần tử của tập hợp đó. Cộng đồng Lisp cũng (không may) sử dụng từ "đóng" để mô tả một khái niệm hoàn toàn không liên quan: Đóng là một kỹ thuật triển khai để biểu diễn các thủ tục với các biến tự do. Chúng tôi không sử dụng từ "đóng" theo nghĩa thứ hai trong cuốn sách này.] Tính chất đóng là chìa khóa cho sức mạnh trong bất kỳ phương tiện kết hợp nào vì nó cho phép chúng ta tạo ra các cấu trúc *phân cấp*—các cấu trúc được tạo thành từ các phần, bản thân các phần đó lại được tạo thành từ các phần, v.v.

Ngay từ đầu [Chương 1](Chapter-1.xhtml#Chapter-1), chúng ta đã sử dụng thiết yếu tính chất đóng trong việc xử lý các thủ tục, vì tất cả các chương trình, ngoại trừ các chương trình đơn giản nhất, đều dựa vào thực tế là các phần tử của một tổ hợp bản thân chúng có thể là các tổ hợp. Trong phần này, chúng ta sẽ xem xét các hệ quả của tính chất đóng đối với dữ liệu phức hợp. Chúng ta mô tả một số kỹ thuật thông thường để sử dụng các cặp để biểu diễn các chuỗi và cây, và chúng ta trưng bày một ngôn ngữ đồ họa minh họa tính chất đóng một cách sinh động.^[Khái niệm rằng một phương tiện kết hợp phải thỏa mãn tính chất đóng là một ý tưởng đơn giản. Thật không may, các bộ kết hợp dữ liệu được cung cấp trong nhiều ngôn ngữ lập trình phổ biến không thỏa mãn tính chất đóng hoặc làm cho việc khai thác tính chất đóng trở nên cồng kềnh. Trong Fortran hoặc Basic, người ta thường kết hợp các phần tử dữ liệu bằng cách lắp ráp chúng thành mảng—nhưng người ta không thể tạo thành các mảng mà các phần tử của bản thân chúng là mảng. Pascal và C thừa nhận các cấu trúc mà các phần tử của bản thân chúng là các cấu trúc. Tuy nhiên, điều này đòi hỏi lập trình viên phải thao tác các con trỏ một cách rõ ràng và tuân theo hạn chế là mỗi trường của một cấu trúc chỉ có thể chứa các phần tử thuộc một dạng được chỉ định trước. Không giống như Lisp với các cặp của nó, các ngôn ngữ này không có chất kết dính đa mục đích tích hợp giúp dễ dàng thao tác dữ liệu phức hợp một cách thống nhất. Hạn chế này nằm sau nhận xét của Alan Perlis trong lời tựa cho cuốn sách này: “Trong Pascal, sự phong phú của các cấu trúc dữ liệu có thể khai báo tạo ra sự chuyên môn hóa trong các hàm, điều này ức chế và trừng phạt sự hợp tác ngẫu nhiên. Tốt hơn là nên có 100 hàm hoạt động trên một cấu trúc dữ liệu hơn là có 10 hàm hoạt động trên 10 cấu trúc dữ liệu.”]

## 2.2.1 Biểu diễn Chuỗi

Một trong những cấu trúc hữu ích mà chúng ta có thể xây dựng bằng các cặp là một *chuỗi*—một tập hợp các đối tượng dữ liệu có thứ tự. Tất nhiên, có nhiều cách để biểu diễn các chuỗi theo các cặp. Một biểu diễn đặc biệt đơn giản được minh họa trong [Hình 2.4](#Figure-2_002e4), trong đó chuỗi 1, 2, 3, 4 được biểu diễn dưới dạng một chuỗi các cặp. `car` của mỗi cặp là mục tương ứng trong chuỗi và `cdr` của cặp là cặp tiếp theo trong chuỗi. `cdr` của cặp cuối cùng báo hiệu sự kết thúc của chuỗi bằng cách trỏ đến một giá trị phân biệt không phải là một cặp, được biểu thị trong sơ đồ hộp và con trỏ dưới dạng một đường chéo và trong các chương trình là giá trị của biến `nil`. Toàn bộ chuỗi được xây dựng bằng các phép toán `cons` lồng nhau:

```scheme
(cons 1
      (cons 2
            (cons 3
                  (cons 4 nil))))
```

![](fig/chap2/Fig2.4e.std.svg 587.4x141.96)
**Hình 2.4:** Chuỗi 1, 2, 3, 4 được biểu diễn dưới dạng một chuỗi các cặp.

Một chuỗi các cặp như vậy, được tạo thành bởi các `cons` lồng nhau, được gọi là *danh sách*, và Scheme cung cấp một nguyên thủy gọi là `list` để giúp xây dựng các danh sách.^[Trong cuốn sách này, chúng ta sử dụng *danh sách* có nghĩa là một chuỗi các cặp kết thúc bằng dấu hiệu kết thúc danh sách. Ngược lại, thuật ngữ *cấu trúc danh sách* đề cập đến bất kỳ cấu trúc dữ liệu nào được tạo thành từ các cặp, không chỉ danh sách.] Chuỗi trên có thể được tạo ra bởi `(list 1 2 3 4)`. Nói chung,

```scheme
(list ⟨a₁⟩ ⟨a₂⟩ … ⟨aₙ⟩)
```

tương đương với

```scheme
(cons ⟨a₁⟩
      (cons ⟨a₂⟩
            (cons …
                  (cons ⟨aₙ⟩
                        nil)…)))
```

Các hệ thống Lisp thông thường in các danh sách bằng cách in chuỗi các phần tử, được đặt trong dấu ngoặc đơn. Do đó, đối tượng dữ liệu trong [Hình 2.4](#Figure-2_002e4) được in là `(1 2 3 4)`:

```scheme
(define one-through-four (list 1 2 3 4))

one-through-four
(1 2 3 4)
```

Hãy cẩn thận đừng nhầm lẫn biểu thức `(list 1 2 3 4)` với danh sách `(1 2 3 4)`, đây là kết quả nhận được khi biểu thức được đánh giá. Cố gắng đánh giá biểu thức `(1 2 3 4)` sẽ báo lỗi khi trình thông dịch cố gắng áp dụng thủ tục `1` cho các đối số `2`, `3`, `4`.

Chúng ta có thể nghĩ về `car` như chọn mục đầu tiên trong danh sách và `cdr` như chọn danh sách con bao gồm tất cả các mục ngoại trừ mục đầu tiên. Các ứng dụng lồng nhau của `car` và `cdr` có thể được sử dụng để trích xuất mục thứ hai, thứ ba và các mục tiếp theo trong danh sách.^[Vì các ứng dụng lồng nhau của `car` và `cdr` rất cồng kềnh khi viết, nên các phương ngữ Lisp cung cấp các chữ viết tắt cho chúng—ví dụ,] Bộ xây dựng `cons` tạo ra một danh sách giống như danh sách ban đầu, nhưng có một mục bổ sung ở đầu.

```scheme
(car one-through-four)
1

(cdr one-through-four)
(2 3 4)

(car (cdr one-through-four))
2

(cons 10 one-through-four)
(10 1 2 3 4)

(cons 5 one-through-four)
(5 1 2 3 4)
```

Giá trị của `nil`, được sử dụng để kết thúc chuỗi các cặp, có thể được coi là một chuỗi không có phần tử nào, *danh sách rỗng*. Từ *nil* là một dạng rút gọn của từ Latin *nihil*, có nghĩa là “không có gì”.^[Thật đáng chú ý là có bao nhiêu năng lượng trong việc chuẩn hóa các phương ngữ Lisp đã bị tiêu tan trong các tranh cãi mà theo nghĩa đen là về không có gì: Liệu `nil` có phải là một tên thông thường không? Giá trị của `nil` có nên là một ký hiệu không? Nó có nên là một danh sách không? Nó có nên là một cặp không? Trong Scheme, `nil` là một tên thông thường, mà chúng ta sử dụng trong phần này như một biến có giá trị là dấu hiệu kết thúc danh sách (giống như `true` là một biến thông thường có giá trị true). Các phương ngữ Lisp khác, bao gồm Common Lisp, coi `nil` là một ký hiệu đặc biệt. Các tác giả của cuốn sách này, những người đã trải qua quá nhiều cuộc tranh cãi về chuẩn hóa ngôn ngữ, muốn tránh toàn bộ vấn đề này. Sau khi chúng ta giới thiệu trích dẫn trong [2.3](2_002e3.xhtml#g_t2_002e3), chúng ta sẽ biểu thị danh sách rỗng là `'()` và loại bỏ hoàn toàn biến `nil`.]

### Các phép toán danh sách

Việc sử dụng các cặp để biểu diễn các chuỗi phần tử dưới dạng danh sách đi kèm với các kỹ thuật lập trình thông thường để thao tác danh sách bằng cách liên tục "`cdr` xuống" các danh sách. Ví dụ: thủ tục `list-ref` nhận các đối số là một danh sách và một số $n$ và trả về mục thứ $n$ của danh sách. Thông thường, các phần tử của danh sách được đánh số bắt đầu bằng 0. Phương pháp tính toán `list-ref` như sau:

- Đối với $n = 0$, `list-ref` sẽ trả về `car` của danh sách.
- Nếu không, `list-ref` sẽ trả về mục thứ $(n - 1)$ của `cdr` của danh sách.

```scheme
(define (list-ref items n)
  (if (= n 0)
      (car items)
      (list-ref (cdr items)
                (- n 1))))

(define squares
  (list 1 4 9 16 25))

(list-ref squares 3)
16
```

Thông thường chúng ta `cdr` xuống toàn bộ danh sách. Để hỗ trợ điều này, Scheme bao gồm một vị từ nguyên thủy `null?`, kiểm tra xem đối số của nó có phải là danh sách rỗng hay không. Thủ tục `length`, trả về số mục trong danh sách, minh họa mẫu sử dụng điển hình này:

```scheme
(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

(define odds
  (list 1 3 5 7))

(length odds)
4
```

Thủ tục `length` triển khai một kế hoạch đệ quy đơn giản. Bước giảm là:

- `length` của bất kỳ danh sách nào là 1 cộng với `length` của `cdr` của danh sách.

Điều này được áp dụng liên tục cho đến khi chúng ta đạt đến trường hợp cơ bản:

- `length` của danh sách rỗng là 0.

Chúng ta cũng có thể tính toán `length` theo kiểu lặp:

```scheme
(define (length items)
  (define (length-iter a count)
    (if (null? a)
        count
        (length-iter (cdr a)
                     (+ 1 count))))
  (length-iter items 0))
```

Một kỹ thuật lập trình thông thường khác là "kết hợp `cons`" một danh sách trả lời trong khi `cdr` xuống một danh sách, như trong thủ tục `append`, nhận hai danh sách làm đối số và kết hợp các phần tử của chúng để tạo thành một danh sách mới:

```scheme
(append squares odds)
(1 4 9 16 25 1 3 5 7)

(append odds squares)
(1 3 5 7 1 4 9 16 25)
```

`Append` cũng được triển khai bằng một kế hoạch đệ quy. Để `append` các danh sách `list1` và `list2`, hãy thực hiện như sau:

- Nếu `list1` là danh sách rỗng, thì kết quả chỉ là `list2`.
- Nếu không, hãy `append` `cdr` của `list1` và `list2`, đồng thời `cons` `car` của `list1` lên kết quả:

```scheme
(define (append list1 list2)
  (if (null? list1)
      list2
      (cons (car list1)
            (append (cdr list1)
                    list2))))
```

**Bài tập 2.17:** Hãy định nghĩa một thủ tục `last-pair` trả về danh sách chỉ chứa phần tử cuối cùng của một danh sách đã cho (không rỗng):

```scheme
(last-pair (list 23 72 149 34))
(34)
```

**Bài tập 2.18:** Hãy định nghĩa một thủ tục `reverse` nhận một danh sách làm đối số và trả về một danh sách các phần tử giống nhau theo thứ tự ngược lại:

```scheme
(reverse (list 1 4 9 16 25))
(25 16 9 4 1)
```

**Bài tập 2.19:** Hãy xem xét chương trình đếm tiền xu của [1.2.2](1_002e2.xhtml#g_t1_002e2_002e2). Sẽ rất tuyệt nếu có thể dễ dàng thay đổi loại tiền tệ mà chương trình sử dụng, để chúng ta có thể tính số cách đổi một bảng Anh chẳng hạn. Như chương trình được viết, kiến thức về loại tiền tệ được phân phối một phần vào thủ tục `first-denomination` và một phần vào thủ tục `count-change` (biết rằng có năm loại tiền xu của Hoa Kỳ). Sẽ tốt hơn nếu có thể cung cấp một danh sách các đồng xu được sử dụng để đổi tiền.

Chúng ta muốn viết lại thủ tục `cc` để đối số thứ hai của nó là danh sách các giá trị của các đồng xu để sử dụng thay vì một số nguyên chỉ định đồng xu nào cần sử dụng. Sau đó, chúng ta có thể có các danh sách xác định từng loại tiền tệ:

```scheme
(define us-coins
  (list 50 25 10 5 1))

(define uk-coins
  (list 100 50 20 10 5 2 1 0.5))
```

Sau đó, chúng ta có thể gọi `cc` như sau:

```scheme
(cc 100 us-coins)
292
```

Để làm điều này, chúng ta sẽ cần thay đổi một chút chương trình `cc`. Nó vẫn sẽ có cùng dạng, nhưng nó sẽ truy cập đối số thứ hai của nó một cách khác, như sau:

```scheme
(define (cc amount coin-values)
  (cond ((= amount 0)
         1)
        ((or (< amount 0)
             (no-more? coin-values))
         0)
        (else
         (+ (cc
             amount
             (except-first-denomination
              coin-values))
            (cc
             (- amount
                (first-denomination
                 coin-values))
             coin-values)))))
```

Hãy định nghĩa các thủ tục `first-denomination`, `except-first-denomination` và `no-more?` theo các phép toán nguyên thủy trên các cấu trúc danh sách. Thứ tự của danh sách `coin-values` có ảnh hưởng đến câu trả lời do `cc` tạo ra không? Tại sao hay tại sao không?

**Bài tập 2.20:** Các thủ tục `+`, `*` và `list` nhận số lượng đối số tùy ý. Một cách để định nghĩa các thủ tục như vậy là sử dụng `define` với *ký hiệu đuôi chấm*. Trong định nghĩa thủ tục, danh sách tham số có dấu chấm trước tên tham số cuối cùng cho biết rằng, khi thủ tục được gọi, các tham số ban đầu (nếu có) sẽ có các giá trị là các đối số ban đầu, như thường lệ, nhưng giá trị của tham số cuối cùng sẽ là *danh sách* của bất kỳ đối số còn lại nào. Ví dụ: cho định nghĩa

```scheme
(define (f x y . z) ⟨body⟩)
```

thủ tục `f` có thể được gọi với hai đối số trở lên. Nếu chúng ta đánh giá

```scheme
(f 1 2 3 4 5 6)
```

thì trong phần thân của `f`, `x` sẽ là 1, `y` sẽ là 2 và `z` sẽ là danh sách `(3 4 5 6)`. Với định nghĩa

```scheme
(define (g . w) ⟨body⟩)
```

thủ tục `g` có thể được gọi với 0 đối số trở lên. Nếu chúng ta đánh giá

```scheme
(g 1 2 3 4 5 6)
```

thì trong phần thân của `g`, `w` sẽ là danh sách `(1 2 3 4 5 6)`.^[Để định nghĩa `f` và `g` bằng cách sử dụng `lambda`, chúng ta sẽ viết]

Sử dụng ký hiệu này để viết một thủ tục `same-parity` nhận một hoặc nhiều số nguyên và trả về một danh sách tất cả các đối số có cùng tính chẵn lẻ như đối số đầu tiên. Ví dụ,

```scheme
(same-parity 1 2 3 4 5 6 7)
(1 3 5 7)

(same-parity 2 3 4 5 6 7)
(2 4 6)
```

### Ánh xạ trên danh sách

Một phép toán cực kỳ hữu ích là áp dụng một số phép biến đổi cho từng phần tử trong danh sách và tạo ra danh sách kết quả. Ví dụ, thủ tục sau đây chia tỷ lệ mỗi số trong một danh sách theo một hệ số đã cho:

```scheme
(define (scale-list items factor)
  (if (null? items)
      nil
      (cons (* (car items) factor)
            (scale-list (cdr items)
                        factor))))

(scale-list (list 1 2 3 4 5) 10)
(10 20 30 40 50)
```

Chúng ta có thể trừu tượng hóa ý tưởng chung này và nắm bắt nó dưới dạng một mẫu chung được thể hiện dưới dạng một thủ tục bậc cao, giống như trong [1.3](1_002e3.xhtml#g_t1_002e3). Thủ tục bậc cao ở đây được gọi là `map`. `Map` nhận các đối số là một thủ tục của một đối số và một danh sách, đồng thời trả về một danh sách các kết quả được tạo ra bằng cách áp dụng thủ tục cho từng phần tử trong danh sách:^[Scheme theo tiêu chuẩn cung cấp một thủ tục `map` tổng quát hơn thủ tục được mô tả ở đây. `map` tổng quát hơn này nhận một thủ tục của $n$ đối số, cùng với $n$ danh sách, và áp dụng thủ tục cho tất cả các phần tử đầu tiên của danh sách, tất cả các phần tử thứ hai của danh sách, v.v., trả về một danh sách các kết quả. Ví dụ:]

```scheme
(define (map proc items)
  (if (null? items)
      nil
      (cons (proc (car items))
            (map proc (cdr items)))))

(map abs (list -10 2.5 -11.6 17))
(10 2.5 11.6 17)

(map (lambda (x) (* x x)) (list 1 2 3 4))
(1 4 9 16)
```

Bây giờ chúng ta có thể đưa ra một định nghĩa mới của `scale-list` theo `map`:

```scheme
(define (scale-list items factor)
  (map (lambda (x) (* x factor))
       items))
```

`Map` là một cấu trúc quan trọng, không chỉ vì nó nắm bắt một mẫu chung, mà vì nó thiết lập một mức độ trừu tượng cao hơn trong việc xử lý các danh sách. Trong định nghĩa ban đầu của `scale-list`, cấu trúc đệ quy của chương trình thu hút sự chú ý đến quá trình xử lý danh sách từng phần tử. Định nghĩa `scale-list` theo `map` sẽ bỏ qua mức độ chi tiết đó và nhấn mạnh rằng việc chia tỷ lệ sẽ biến đổi một danh sách các phần tử thành một danh sách các kết quả. Sự khác biệt giữa hai định nghĩa không phải là máy tính đang thực hiện một quy trình khác (không phải vậy) mà là chúng ta suy nghĩ về quy trình đó một cách khác. Trên thực tế, `map` giúp thiết lập một rào cản trừu tượng cô lập việc triển khai các thủ tục chuyển đổi danh sách khỏi các chi tiết về cách các phần tử của danh sách được trích xuất và kết hợp. Giống như các rào cản được hiển thị trong [Hình 2.1](2_002e1.xhtml#Figure-2_002e1), trừu tượng này mang lại cho chúng ta sự linh hoạt để thay đổi các chi tiết cấp thấp về cách các chuỗi được triển khai, đồng thời bảo toàn khuôn khổ khái niệm về các phép toán biến đổi các chuỗi thành các chuỗi. Phần [2.2.3](#g_t2_002e2_002e3) mở rộng việc sử dụng các chuỗi này như một khuôn khổ để tổ chức các chương trình.

**Bài tập 2.21:** Thủ tục `square-list` nhận một danh sách các số làm đối số và trả về một danh sách các bình phương của các số đó.

```scheme
(square-list (list 1 2 3 4))
(1 4 9 16)
```

Đây là hai định nghĩa khác nhau của `square-list`. Hãy hoàn thành cả hai bằng cách điền vào các biểu thức bị thiếu:

```scheme
(define (square-list items)
  (if (null? items)
      nil
      (cons ⟨??⟩ ⟨??⟩)))

(define (square-list items)
  (map ⟨??⟩ ⟨??⟩))
```

**Bài tập 2.22:** Louis Reasoner cố gắng viết lại thủ tục `square-list` đầu tiên của [Bài tập 2.21](#Exercise-2_002e21) để nó phát triển một quá trình lặp:

```scheme
(define (square-list items)
  (define (iter things answer)
    (if (null? things)
        answer
        (iter (cdr things)
              (cons (square (car things))
                    answer))))
  (iter items nil))
```

Thật không may, việc định nghĩa `square-list` theo cách này tạo ra danh sách trả lời theo thứ tự ngược lại so với danh sách mong muốn. Tại sao?

Sau đó, Louis cố gắng sửa lỗi bằng cách hoán đổi các đối số cho `cons`:

```scheme
(define (square-list items)
  (define (iter things answer)
    (if (null? things)
        answer
        (iter (cdr things)
              (cons answer
                    (square
                     (car things))))))
  (iter items nil))
```

Điều này cũng không hoạt động. Hãy giải thích.

**Bài tập 2.23:** Thủ tục `for-each` tương tự như `map`. Nó nhận các đối số là một thủ tục và một danh sách các phần tử. Tuy nhiên, thay vì tạo thành một danh sách các kết quả, `for-each` chỉ áp dụng thủ tục cho từng phần tử theo thứ tự, từ trái sang phải. Các giá trị được trả về khi áp dụng thủ tục cho các phần tử không được sử dụng chút nào—`for-each` được sử dụng với các thủ tục thực hiện một hành động, chẳng hạn như in. Ví dụ,

```scheme
(for-each
 (lambda (x) (newline) (display x))
 (list 57 321 88))

57
321
88
```

Giá trị được trả về bởi lệnh gọi đến `for-each` (không được minh họa ở trên) có thể là một thứ tùy ý, chẳng hạn như true. Hãy cung cấp một cách triển khai của `for-each`.

## 2.2.2 Cấu trúc Phân cấp

Biểu diễn các chuỗi theo danh sách được khái quát một cách tự nhiên để biểu diễn các chuỗi mà các phần tử của bản thân chúng có thể là các chuỗi. Ví dụ, chúng ta có thể coi đối tượng `((1 2) 3 4)` được xây dựng bởi

```scheme
(cons (list 1 2) (list 3 4))
```

là một danh sách gồm ba mục, mục đầu tiên bản thân nó là một danh sách, `(1 2)`. Thật vậy, điều này được gợi ý bởi dạng mà kết quả được in bởi trình thông dịch. [Hình 2.5](#Figure-2_002e5) cho thấy biểu diễn của cấu trúc này theo các cặp.

![](fig/chap2/Fig2.5e.std.svg 622.68x308.76)
**Hình 2.5:** Cấu trúc được tạo bởi `(cons (list 1 2) (list 3 4))`.

Một cách khác để nghĩ về các chuỗi mà các phần tử là các chuỗi là *cây*. Các phần tử của chuỗi là các nhánh của cây và các phần tử bản thân chúng là các chuỗi là các cây con. [Hình 2.6](#Figure-2_002e6) cho thấy cấu trúc trong [Hình 2.5](#Figure-2_002e5) được xem như một cây.

![](fig/chap2/Fig2.6b.std.svg 180.24x204.12)
**Hình 2.6:** Cấu trúc danh sách trong [Hình 2.5](#Figure-2_002e5) được xem như một cây.

Đệ quy là một công cụ tự nhiên để xử lý các cấu trúc cây, vì chúng ta thường có thể giảm các phép toán trên cây thành các phép toán trên các nhánh của chúng, lần lượt giảm xuống các phép toán trên các nhánh của các nhánh, v.v., cho đến khi chúng ta đạt đến các lá của cây. Ví dụ: hãy so sánh thủ tục `length` của [2.2.1](#g_t2_002e2_002e1) với thủ tục `count-leaves`, trả về tổng số lá của một cây:

```scheme
(define x (cons (list 1 2) (list 3 4)))
```

```scheme
(length x)
3
```

```scheme
(count-leaves x)
4

(list x x)
(((1 2) 3 4) ((1 2) 3 4))

(length (list x x))
2

(count-leaves (list x x))
8
```

Để triển khai `count-leaves`, hãy nhớ lại kế hoạch đệ quy để tính `length`:

- `Length` của một danh sách `x` là 1 cộng với `length` của `cdr` của `x`.
- `Length` của danh sách rỗng là 0.

`Count-leaves` tương tự. Giá trị cho danh sách rỗng là giống nhau:

- `Count-leaves` của danh sách rỗng là 0.

Nhưng trong bước giảm, nơi chúng ta loại bỏ `car` của danh sách, chúng ta phải tính đến việc `car` bản thân nó có thể là một cây mà chúng ta cần đếm số lá của nó. Do đó, bước giảm thích hợp là

- `Count-leaves` của một cây `x` là `count-leaves` của `car` của `x` cộng với `count-leaves` của `cdr` của `x`.

Cuối cùng, bằng cách lấy `car`s, chúng ta đạt đến các lá thực tế, vì vậy chúng ta cần một trường hợp cơ bản khác:

- `Count-leaves` của một lá là 1.

Để hỗ trợ viết các thủ tục đệ quy trên cây, Scheme cung cấp vị từ nguyên thủy `pair?`, kiểm tra xem đối số của nó có phải là một cặp hay không. Đây là thủ tục hoàn chỉnh:^[Thứ tự của hai mệnh đề đầu tiên trong `cond` là quan trọng, vì danh sách rỗng thỏa mãn `null?` và cũng không phải là một cặp.]

```scheme
(define (count-leaves x)
  (cond ((null? x) 0)
        ((not (pair? x)) 1)
        (else (+ (count-leaves (car x))
                 (count-leaves (cdr x))))))
```

**Bài tập 2.24:** Giả sử chúng ta đánh giá biểu thức `(list 1 (list 2 (list 3 4)))`. Hãy đưa ra kết quả được in bởi trình thông dịch, cấu trúc hộp và con trỏ tương ứng và cách diễn giải nó như một cây (như trong [Hình 2.6](#Figure-2_002e6)).

**Bài tập 2.25:** Hãy đưa ra các tổ hợp của `car`s và `cdr`s sẽ chọn 7 từ mỗi danh sách sau:

```scheme
(1 3 (5 7) 9)
((7))
(1 (2 (3 (4 (5 (6 7))))))
```

**Bài tập 2.26:** Giả sử chúng ta định nghĩa `x` và `y` là hai danh sách:

```scheme
(define x (list 1 2 3))
(define y (list 4 5 6))
```

Kết quả nào được in bởi trình thông dịch để đáp lại việc đánh giá từng biểu thức sau:

```scheme
(append x y)
(cons x y)
(list x y)
```

**Bài tập 2.27:** Hãy sửa đổi thủ tục `reverse` của bạn từ [Bài tập 2.18](#Exercise-2_002e18) để tạo ra một thủ tục `deep-reverse` nhận một danh sách làm đối số và trả về giá trị của nó là danh sách với các phần tử của nó bị đảo ngược và tất cả các danh sách con cũng bị đảo ngược sâu. Ví dụ,

```scheme
(define x
  (list (list 1 2) (list 3 4)))

x
((1 2) (3 4))

(reverse x)
((3 4) (1 2))

(deep-reverse x)
((4 3) (2 1))
```

**Bài tập 2.28:** Hãy viết một thủ tục `fringe` nhận một cây (được biểu diễn dưới dạng danh sách) làm đối số và trả về một danh sách mà các phần tử của nó là tất cả các lá của cây được sắp xếp theo thứ tự từ trái sang phải. Ví dụ,

```scheme
(define x
  (list (list 1 2) (list 3 4)))

(fringe x)
(1 2 3 4)

(fringe (list x x))
(1 2 3 4 1 2 3 4)
```

**Bài tập 2.29:** Một mô-bin nhị phân bao gồm hai nhánh, một nhánh bên trái và một nhánh bên phải. Mỗi nhánh là một thanh có độ dài nhất định, mà từ đó treo một quả nặng hoặc một mô-bin nhị phân khác. Chúng ta có thể biểu diễn một mô-bin nhị phân bằng dữ liệu phức hợp bằng cách xây dựng nó từ hai nhánh (ví dụ: bằng cách sử dụng `list`):

```scheme
(define (make-mobile left right)
  (list left right))
```

Một nhánh được xây dựng từ `length` (phải là một số) cùng với `structure`, có thể là một số (đại diện cho một quả nặng đơn giản) hoặc một mô-bin khác:

```scheme
(define (make-branch length structure)
  (list length structure))
```

1.  Hãy viết các bộ chọn tương ứng `left-branch` và `right-branch`, trả về các nhánh của một mô-bin, và `branch-length` và `branch-structure`, trả về các thành phần của một nhánh.
2.  Sử dụng các bộ chọn của bạn, hãy định nghĩa một thủ tục `total-weight` trả về tổng trọng lượng của một mô-bin.
3.  Một mô-bin được cho là *cân bằng* nếu mô-men xoắn do nhánh trên cùng bên trái của nó tác dụng bằng với mô-men xoắn do nhánh trên cùng bên phải của nó tác dụng (tức là, nếu độ dài của thanh bên trái nhân với trọng lượng treo từ thanh đó bằng với tích tương ứng cho bên phải) và nếu mỗi mô-bin phụ treo trên các nhánh của nó được cân bằng. Hãy thiết kế một vị từ để kiểm tra xem một mô-bin nhị phân có cân bằng hay không.
4.  Giả sử chúng ta thay đổi biểu diễn của các mô-bin để các bộ xây dựng là

    ```scheme
    (define (make-mobile left right)
      (cons left right))

    (define (make-branch length structure)
      (cons length structure))
    ```

    Bạn cần thay đổi bao nhiêu chương trình của mình để chuyển sang biểu diễn mới?

Chắc chắn rồi, đây là phần tiếp theo của bản dịch tiếng Việt, hoàn thành đoạn văn bản bạn đã cung cấp:

### Ánh xạ trên cây (tiếp tục)

Cũng giống như `map` là một trừu tượng mạnh mẽ để xử lý các chuỗi, `map` cùng với đệ quy là một trừu tượng mạnh mẽ để xử lý cây. Ví dụ, thủ tục `scale-tree`, tương tự như `scale-list` của [2.2.1](#g_t2_002e2_002e1), nhận các đối số là một hệ số số và một cây mà các lá là các số. Nó trả về một cây có cùng hình dạng, trong đó mỗi số được nhân với hệ số. Kế hoạch đệ quy cho `scale-tree` tương tự như kế hoạch cho `count-leaves`:

```scheme
(define (scale-tree tree factor)
  (cond ((null? tree) nil)
        ((not (pair? tree))
         (* tree factor))
        (else
         (cons (scale-tree (car tree)
                           factor)
               (scale-tree (cdr tree)
                           factor)))))

(scale-tree (list 1
                  (list 2 (list 3 4) 5)
                  (list 6 7))
            10)

(10 (20 (30 40) 50) (60 70))
```

Một cách khác để triển khai `scale-tree` là coi cây như một chuỗi các cây con và sử dụng `map`. Chúng ta ánh xạ trên chuỗi, chia tỷ lệ từng cây con và trả về danh sách kết quả. Trong trường hợp cơ bản, khi cây là một lá, chúng ta chỉ cần nhân với hệ số:

```scheme
(define (scale-tree tree factor)
  (map (lambda (sub-tree)
         (if (pair? sub-tree)
             (scale-tree sub-tree factor)
             (* sub-tree factor)))
       tree))
```

Nhiều phép toán trên cây có thể được triển khai bằng các kết hợp tương tự của các phép toán chuỗi và đệ quy.

**Bài tập 2.30:** Hãy định nghĩa một thủ tục `square-tree` tương tự như thủ tục `square-list` của [Bài tập 2.21](#Exercise-2_002e21). Tức là, `square-tree` nên hoạt động như sau:

```scheme
(square-tree
 (list 1
       (list 2 (list 3 4) 5)
       (list 6 7)))
(1 (4 (9 16) 25) (36 49))
```

Hãy định nghĩa `square-tree` cả trực tiếp (tức là, không sử dụng bất kỳ thủ tục bậc cao nào) và bằng cách sử dụng `map` và đệ quy.

**Bài tập 2.31:** Hãy trừu tượng hóa câu trả lời của bạn cho [Bài tập 2.30](#Exercise-2_002e30) để tạo ra một thủ tục `tree-map` có thuộc tính là `square-tree` có thể được định nghĩa là

```scheme
(define (square-tree tree)
  (tree-map square tree))
```

**Bài tập 2.32:** Chúng ta có thể biểu diễn một tập hợp dưới dạng một danh sách các phần tử riêng biệt và chúng ta có thể biểu diễn tập hợp tất cả các tập hợp con của tập hợp dưới dạng một danh sách các danh sách. Ví dụ: nếu tập hợp là `(1 2 3)`, thì tập hợp tất cả các tập hợp con là `(() (3) (2) (2 3) (1) (1 3) (1 2) (1 2 3))`. Hoàn thành định nghĩa sau của một thủ tục tạo ra tập hợp các tập hợp con của một tập hợp và đưa ra một giải thích rõ ràng về lý do tại sao nó hoạt động:

```scheme
(define (subsets s)
  (if (null? s)
      (list nil)
      (let ((rest (subsets (cdr s))))
        (append rest (map ⟨??⟩ rest)))))
```

## 2.2.3 Các Chuỗi như Giao diện Thông thường

Trong khi làm việc với dữ liệu phức hợp, chúng ta đã nhấn mạnh cách trừu tượng hóa dữ liệu cho phép chúng ta thiết kế các chương trình mà không bị sa lầy vào các chi tiết của biểu diễn dữ liệu và cách trừu tượng hóa bảo toàn cho chúng ta sự linh hoạt để thử nghiệm với các biểu diễn thay thế. Trong phần này, chúng ta giới thiệu một nguyên tắc thiết kế mạnh mẽ khác để làm việc với cấu trúc dữ liệu—việc sử dụng *giao diện thông thường*.

Trong [1.3](1_002e3.xhtml#g_t1_002e3), chúng ta đã thấy cách các trừu tượng chương trình, được triển khai dưới dạng các thủ tục bậc cao, có thể nắm bắt các mẫu chung trong các chương trình xử lý dữ liệu số. Khả năng của chúng ta để xây dựng các phép toán tương tự để làm việc với dữ liệu phức hợp phụ thuộc chủ yếu vào kiểu mà chúng ta thao tác các cấu trúc dữ liệu của mình. Ví dụ: hãy xem xét thủ tục sau, tương tự như thủ tục `count-leaves` của [2.2.2](#g_t2_002e2_002e2), nhận một cây làm đối số và tính tổng bình phương của các lá là số lẻ:

```scheme
(define (sum-odd-squares tree)
  (cond ((null? tree) 0)
        ((not (pair? tree))
         (if (odd? tree) (square tree) 0))
        (else (+ (sum-odd-squares
                  (car tree))
                 (sum-odd-squares
                  (cdr tree))))))
```

Trên bề mặt, thủ tục này rất khác với thủ tục sau, tạo ra một danh sách tất cả các số Fibonacci chẵn $\text{Fib}(k)$, trong đó $k$ nhỏ hơn hoặc bằng một số nguyên $n$ đã cho:

```scheme
(define (even-fibs n)
  (define (next k)
    (if (> k n)
        nil
        (let ((f (fib k)))
          (if (even? f)
              (cons f (next (+ k 1)))
              (next (+ k 1))))))
  (next 0))
```

Mặc dù thực tế là hai thủ tục này có cấu trúc rất khác nhau, nhưng một mô tả trừu tượng hơn về hai tính toán cho thấy rất nhiều điểm tương đồng. Chương trình đầu tiên

- liệt kê các lá của một cây;
- lọc chúng, chọn những số lẻ;
- bình phương từng số đã chọn; và
- tích lũy kết quả bằng cách sử dụng `+`, bắt đầu bằng 0.

Chương trình thứ hai

- liệt kê các số nguyên từ 0 đến $n$;
- tính số Fibonacci cho mỗi số nguyên;
- lọc chúng, chọn những số chẵn; và
- tích lũy kết quả bằng cách sử dụng `cons`, bắt đầu bằng danh sách rỗng.

Một kỹ sư xử lý tín hiệu sẽ thấy tự nhiên khi khái niệm hóa các quy trình này theo các tín hiệu chảy qua một tầng các giai đoạn, mỗi giai đoạn thực hiện một phần của kế hoạch chương trình, như được hiển thị trong [Hình 2.7](#Figure-2_002e7). Trong `sum-odd-squares`, chúng ta bắt đầu với một *bộ liệt kê*, tạo ra một "tín hiệu" bao gồm các lá của một cây đã cho. Tín hiệu này được truyền qua một *bộ lọc*, loại bỏ tất cả các phần tử trừ số lẻ. Tín hiệu kết quả lần lượt được truyền qua một *ánh xạ*, đây là một "bộ chuyển đổi" áp dụng thủ tục `square` cho từng phần tử. Đầu ra của ánh xạ sau đó được đưa vào một *bộ tích lũy*, kết hợp các phần tử bằng cách sử dụng `+`, bắt đầu từ 0 ban đầu. Kế hoạch cho `even-fibs` là tương tự.

![](fig/chap2/Fig2.7e.std.svg 695.16x194.76)
**Hình 2.7:** Các kế hoạch luồng tín hiệu cho các thủ tục `sum-odd-squares` (trên cùng) và `even-fibs` (dưới cùng) cho thấy điểm chung giữa hai chương trình.

Thật không may, hai định nghĩa thủ tục trên không thể hiện cấu trúc luồng tín hiệu này. Ví dụ: nếu chúng ta kiểm tra thủ tục `sum-odd-squares`, chúng ta thấy rằng việc liệt kê được thực hiện một phần bởi các kiểm tra `null?` và `pair?` và một phần bởi cấu trúc đệ quy cây của thủ tục. Tương tự, sự tích lũy được tìm thấy một phần trong các kiểm tra và một phần trong phép cộng được sử dụng trong đệ quy. Nói chung, không có các phần riêng biệt của một trong hai thủ tục tương ứng với các phần tử trong mô tả luồng tín hiệu. Hai thủ tục của chúng ta phân tách các tính toán theo một cách khác, trải việc liệt kê trên chương trình và trộn nó với ánh xạ, bộ lọc và sự tích lũy. Nếu chúng ta có thể tổ chức các chương trình của mình để làm cho cấu trúc luồng tín hiệu biểu hiện trong các thủ tục chúng ta viết, điều này sẽ làm tăng tính rõ ràng về khái niệm của mã kết quả.

### Các Phép Toán Chuỗi

Chìa khóa để tổ chức các chương trình để phản ánh rõ ràng hơn cấu trúc luồng tín hiệu là tập trung vào các "tín hiệu" chảy từ giai đoạn này sang giai đoạn khác trong quy trình. Nếu chúng ta biểu diễn các tín hiệu này dưới dạng danh sách, thì chúng ta có thể sử dụng các phép toán danh sách để triển khai việc xử lý ở mỗi giai đoạn. Ví dụ: chúng ta có thể triển khai các giai đoạn ánh xạ của sơ đồ luồng tín hiệu bằng cách sử dụng thủ tục `map` từ [2.2.1](#g_t2_002e2_002e1):

```scheme
(map square (list 1 2 3 4 5))
(1 4 9 16 25)
```

Việc lọc một chuỗi để chọn chỉ những phần tử thỏa mãn một vị từ đã cho được thực hiện bằng

```scheme
(define (filter predicate sequence)
  (cond ((null? sequence) nil)
        ((predicate (car sequence))
         (cons (car sequence)
               (filter predicate
                       (cdr sequence))))
        (else (filter predicate
                       (cdr sequence)))))
```

Ví dụ,

```scheme
(filter odd? (list 1 2 3 4 5))
(1 3 5)
```

Sự tích lũy có thể được triển khai bằng

```scheme
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op
                      initial
                      (cdr sequence)))))

(accumulate + 0 (list 1 2 3 4 5))
15
(accumulate * 1 (list 1 2 3 4 5))
120
(accumulate cons nil (list 1 2 3 4 5))
(1 2 3 4 5)
```

Tất cả những gì còn lại để triển khai các sơ đồ luồng tín hiệu là liệt kê chuỗi các phần tử sẽ được xử lý. Đối với `even-fibs`, chúng ta cần tạo chuỗi các số nguyên trong một phạm vi đã cho, mà chúng ta có thể làm như sau:

```scheme
(define (enumerate-interval low high)
  (if (> low high)
      nil
      (cons low
            (enumerate-interval
             (+ low 1)
             high))))

(enumerate-interval 2 7)
(2 3 4 5 6 7)
```

Để liệt kê các lá của một cây, chúng ta có thể sử dụng^[Trên thực tế, đây chính xác là thủ tục `fringe` từ [Bài tập 2.28](#Exercise-2_002e28). Ở đây chúng ta đã đổi tên nó để nhấn mạnh rằng nó là một phần của một họ các thủ tục thao tác chuỗi chung.]

```scheme
(define (enumerate-tree tree)
  (cond ((null? tree) nil)
        ((not (pair? tree)) (list tree))
        (else (append
               (enumerate-tree (car tree))
               (enumerate-tree (cdr tree))))))

(enumerate-tree (list 1 (list 2 (list 3 4)) 5))
(1 2 3 4 5)
```

Bây giờ chúng ta có thể viết lại `sum-odd-squares` và `even-fibs` như trong sơ đồ luồng tín hiệu. Đối với `sum-odd-squares`, chúng ta liệt kê chuỗi các lá của cây, lọc nó để chỉ giữ lại các số lẻ trong chuỗi, bình phương từng phần tử và tính tổng kết quả:

```scheme
(define (sum-odd-squares tree)
  (accumulate
   +
   0
   (map square
        (filter odd?
                (enumerate-tree tree)))))
```

Đối với `even-fibs`, chúng ta liệt kê các số nguyên từ 0 đến $n$, tạo số Fibonacci cho mỗi số nguyên này, lọc chuỗi kết quả để chỉ giữ lại các phần tử chẵn và tích lũy kết quả vào một danh sách:

```scheme
(define (even-fibs n)
  (accumulate
   cons
   nil
   (filter even?
           (map fib
                (enumerate-interval 0 n)))))
```

Giá trị của việc biểu thị các chương trình dưới dạng các phép toán chuỗi là điều này giúp chúng ta tạo ra các thiết kế chương trình mang tính mô-đun, tức là các thiết kế được xây dựng bằng cách kết hợp các phần tương đối độc lập. Chúng ta có thể khuyến khích thiết kế mô-đun bằng cách cung cấp một thư viện các thành phần tiêu chuẩn cùng với một giao diện thông thường để kết nối các thành phần theo những cách linh hoạt.

Xây dựng mô-đun là một chiến lược mạnh mẽ để kiểm soát sự phức tạp trong thiết kế kỹ thuật. Ví dụ, trong các ứng dụng xử lý tín hiệu thực tế, các nhà thiết kế thường xuyên xây dựng hệ thống bằng cách xếp tầng các phần tử được chọn từ các họ bộ lọc và bộ chuyển đổi tiêu chuẩn. Tương tự, các phép toán chuỗi cung cấp một thư viện các phần tử chương trình tiêu chuẩn mà chúng ta có thể trộn và kết hợp. Ví dụ: chúng ta có thể sử dụng lại các phần từ các thủ tục `sum-odd-squares` và `even-fibs` trong một chương trình tạo ra danh sách bình phương của $n+1$ số Fibonacci đầu tiên:

```scheme
(define (list-fib-squares n)
  (accumulate
   cons
   nil
   (map square
        (map fib
             (enumerate-interval 0 n)))))

(list-fib-squares 10)
(0 1 1 4 9 25 64 169 441 1156 3025)
```

Chúng ta có thể sắp xếp lại các phần và sử dụng chúng để tính tích các bình phương của các số nguyên lẻ trong một chuỗi:

```scheme
(define
  (product-of-squares-of-odd-elements
   sequence)
  (accumulate
   *
   1
   (map square (filter odd? sequence))))

(product-of-squares-of-odd-elements
 (list 1 2 3 4 5))
225
```

Chúng ta cũng có thể xây dựng các ứng dụng xử lý dữ liệu thông thường theo các phép toán chuỗi. Giả sử chúng ta có một chuỗi hồ sơ nhân sự và chúng ta muốn tìm mức lương của lập trình viên được trả lương cao nhất. Giả sử rằng chúng ta có một bộ chọn `salary` trả về mức lương của một bản ghi và một vị từ `programmer?` kiểm tra xem một bản ghi có phải dành cho lập trình viên hay không. Sau đó, chúng ta có thể viết

```scheme
(define
  (salary-of-highest-paid-programmer
   records)
  (accumulate
   max
   0
   (map salary
        (filter programmer? records))))
```

Những ví dụ này chỉ đưa ra một gợi ý về phạm vi rộng lớn của các phép toán có thể được biểu thị dưới dạng các phép toán chuỗi.^[Richard [Waters (1979)](References.xhtml#Waters-_00281979_0029) đã phát triển một chương trình tự động phân tích các chương trình Fortran truyền thống, xem chúng theo ánh xạ, bộ lọc và tích lũy. Ông thấy rằng 90% mã trong Gói Chương trình con Khoa học Fortran hoàn toàn phù hợp với mô hình này. Một trong những lý do cho sự thành công của Lisp với tư cách là một ngôn ngữ lập trình là danh sách cung cấp một phương tiện tiêu chuẩn để biểu thị các tập hợp có thứ tự để chúng có thể được thao tác bằng các phép toán bậc cao. Ngôn ngữ lập trình APL có được phần lớn sức mạnh và sự hấp dẫn của nó nhờ một lựa chọn tương tự. Trong APL, tất cả dữ liệu được biểu diễn dưới dạng mảng và có một tập hợp các toán tử chung phổ quát và tiện lợi cho tất cả các loại phép toán mảng.]

Các chuỗi, được triển khai ở đây dưới dạng danh sách, đóng vai trò là một giao diện thông thường cho phép chúng ta kết hợp các mô-đun xử lý. Ngoài ra, khi chúng ta biểu diễn các cấu trúc một cách đồng nhất dưới dạng chuỗi, chúng ta đã bản địa hóa các phần phụ thuộc vào cấu trúc dữ liệu trong các chương trình của mình thành một số ít các phép toán chuỗi. Bằng cách thay đổi các phép toán này, chúng ta có thể thử nghiệm các cách biểu diễn thay thế của chuỗi, đồng thời giữ nguyên thiết kế tổng thể của các chương trình. Chúng ta sẽ khai thác khả năng này trong [3.5](3_002e5.xhtml#g_t3_002e5), khi chúng ta tổng quát mô hình xử lý chuỗi để chấp nhận các chuỗi vô hạn.

**Bài tập 2.33:** Hãy điền vào các biểu thức bị thiếu để hoàn thành các định nghĩa sau về một số phép toán thao tác danh sách cơ bản dưới dạng các tích lũy:

```scheme
(define (map p sequence)
  (accumulate (lambda (x y) ⟨??⟩)
              nil sequence))

(define (append seq1 seq2)
  (accumulate cons ⟨??⟩ ⟨??⟩))

(define (length sequence)
  (accumulate ⟨??⟩ 0 sequence))
```

**Bài tập 2.34:** Việc đánh giá một đa thức theo $x$ tại một giá trị đã cho của $x$ có thể được xây dựng dưới dạng một tích lũy. Chúng ta đánh giá đa thức

$${a_{n}x^{n}} + {a_{n - 1}x^{n - 1}} + \cdots + {a_{1}x} + a_{0}$$

bằng cách sử dụng một thuật toán nổi tiếng gọi là *quy tắc Horner*, cấu trúc tính toán là

$${(\ldots(a_{n}x} + {a_{n - 1})x} + \cdots + {a_{1})x} + {a_{0}.}$$

 Nói cách khác, chúng ta bắt đầu với $a_{n}$, nhân với $x$, cộng $a_{n - 1}$, nhân với $x$, v.v., cho đến khi chúng ta đạt đến $a_{0}$.^[Theo [Knuth 1981](References.xhtml#Knuth-1981), quy tắc này được W. G. Horner xây dựng vào đầu thế kỷ XIX, nhưng phương pháp này thực sự đã được Newton sử dụng hơn một trăm năm trước đó. Quy tắc Horner đánh giá đa thức bằng cách sử dụng ít phép cộng và phép nhân hơn so với phương pháp đơn giản là trước tiên tính $a_{n}x^{n}$, sau đó cộng $a_{n - 1}x^{n - 1}$, v.v. Trên thực tế, có thể chứng minh rằng bất kỳ thuật toán nào để đánh giá các đa thức tùy ý phải sử dụng ít nhất nhiều phép cộng và phép nhân như quy tắc Horner, và do đó, quy tắc Horner là một thuật toán tối ưu để đánh giá đa thức. Điều này đã được A. M. Ostrowski chứng minh (đối với số lượng phép cộng) trong một bài báo năm 1954 về cơ bản đã đặt nền móng cho nghiên cứu hiện đại về các thuật toán tối ưu. Tuyên bố tương tự cho các phép nhân đã được V. Y. Pan chứng minh vào năm 1966. Cuốn sách của [Borodin and Munro (1975)](References.xhtml#Borodin-and-Munro-_00281975_0029) cung cấp một cái nhìn tổng quan về những điều này và các kết quả khác về các thuật toán tối ưu.]

Hãy điền vào mẫu sau để tạo ra một thủ tục đánh giá một đa thức bằng quy tắc Horner. Giả sử rằng các hệ số của đa thức được sắp xếp theo một chuỗi, từ $a_{0}$ đến $a_{n}$.

```scheme
(define
  (horner-eval x coefficient-sequence)
  (accumulate
   (lambda (this-coeff higher-terms)
     ⟨??⟩)
   0
   coefficient-sequence))
```

Ví dụ: để tính toán ${1 + 3x} + {5x^{3} + x^{5}}$ tại $x = 2$, bạn sẽ đánh giá

```scheme
(horner-eval 2 (list 1 3 0 5 0 1))
```

**Bài tập 2.35:** Hãy định nghĩa lại `count-leaves` từ [2.2.2](#g_t2_002e2_002e2) như một tích lũy:

```scheme
(define (count-leaves t)
  (accumulate ⟨??⟩ ⟨??⟩ (map ⟨??⟩ ⟨??⟩)))
```

**Bài tập 2.36:** Thủ tục `accumulate-n` tương tự như `accumulate`, ngoại trừ việc nó nhận một chuỗi các chuỗi làm đối số thứ ba, tất cả đều được giả định là có cùng số lượng phần tử. Nó áp dụng thủ tục tích lũy được chỉ định để kết hợp tất cả các phần tử đầu tiên của các chuỗi, tất cả các phần tử thứ hai của các chuỗi, v.v. và trả về một chuỗi các kết quả. Ví dụ: nếu `s` là một chuỗi chứa bốn chuỗi, `((1 2 3) (4 5 6) (7 8 9) (10 11 12)),` thì giá trị của `(accumulate-n + 0 s)` sẽ là chuỗi `(22 26 30)`. Hãy điền vào các biểu thức bị thiếu trong định nghĩa sau của `accumulate-n`:

```scheme
(define (accumulate-n op init seqs)
  (if (null? (car seqs))
      nil
      (cons (accumulate op init ⟨??⟩)
            (accumulate-n op init ⟨??⟩))))
```

**Bài tập 2.37:** Giả sử chúng ta biểu diễn các vectơ **v** = $(v_{i})$ dưới dạng các chuỗi số và các ma trận **m** = $(m_{ij})$ dưới dạng các chuỗi vectơ (các hàng của ma trận). Ví dụ, ma trận

$$\left( \begin{array}{llll}
1 & 2 & 3 & 4 \\
4 & 5 & 6 & 6 \\
6 & 7 & 8 & 9 \\
\end{array} \right)$$

được biểu diễn dưới dạng chuỗi `((1 2 3 4) (4 5 6 6) (6 7 8 9))`. Với biểu diễn này, chúng ta có thể sử dụng các phép toán chuỗi để biểu thị ngắn gọn các phép toán ma trận và vectơ cơ bản. Các phép toán này (được mô tả trong bất kỳ cuốn sách nào về đại số ma trận) như sau:

$$\begin{array}{ll}
\text{(dot-product\ v\ w)} & {\text{trả về tổng}\;\Sigma_{i}v_{i}w_{i};} \\
\text{(matrix-*-vector\ m\ v)} & {\text{trả về vectơ}\;\mathbf{t},} \\
 & {\text{trong đó}\; t_{i} = \Sigma_{j}m_{ij}v_{j};} \\
\text{(matrix-*-matrix\ m\ n)} & {\text{trả về ma trận}\;\mathbf{p},} \\
 & {\text{trong đó}\; p_{ij} = \Sigma_{k}m_{ik}n_{kj};} \\
\text{(transpose\ m)} & {\text{trả về ma trận}\;\mathbf{n},} \\
 & {\text{trong đó}\; n_{ij} = m_{ji}.} \\
\end{array}$$

 Chúng ta có thể định nghĩa tích vô hướng là^[Định nghĩa này sử dụng phiên bản mở rộng của `map` được mô tả trong [Chú thích 78](#Footnote-78).]

```scheme
(define (dot-product v w)
  (accumulate + 0 (map * v w)))
```

Hãy điền vào các biểu thức bị thiếu trong các thủ tục sau để tính các phép toán ma trận khác. (Thủ tục `accumulate-n` được định nghĩa trong [Bài tập 2.36](#Exercise-2_002e36).)

```scheme
(define (matrix-*-vector m v)
  (map ⟨??⟩ m))

(define (transpose mat)
  (accumulate-n ⟨??⟩ ⟨??⟩ mat))

(define (matrix-*-matrix m n)
  (let ((cols (transpose n)))
    (map ⟨??⟩ m)))
```

**Bài tập 2.38:** Thủ tục `accumulate` còn được gọi là `fold-right`, vì nó kết hợp phần tử đầu tiên của chuỗi với kết quả của việc kết hợp tất cả các phần tử ở bên phải. Cũng có một `fold-left`, tương tự như `fold-right`, ngoại trừ việc nó kết hợp các phần tử theo hướng ngược lại:

```scheme
(define (fold-left op initial sequence)
  (define (iter result rest)
    (if (null? rest)
        result
        (iter (op result (car rest))
              (cdr rest))))
  (iter initial sequence))
```

Giá trị của

```scheme
(fold-right / 1 (list 1 2 3))
(fold-left  / 1 (list 1 2 3))
(fold-right list nil (list 1 2 3))
(fold-left  list nil (list 1 2 3))
```

là gì? Hãy đưa ra một thuộc tính mà `op` phải thỏa mãn để đảm bảo rằng `fold-right` và `fold-left` sẽ tạo ra các giá trị giống nhau cho bất kỳ chuỗi nào.

**Bài tập 2.39:** Hoàn thành các định nghĩa sau của `reverse` ([Bài tập 2.18](#Exercise-2_002e18)) theo `fold-right` và `fold-left` từ [Bài tập 2.38](#Exercise-2_002e38):

```scheme
(define (reverse sequence)
  (fold-right
   (lambda (x y) ⟨??⟩) nil sequence))

(define (reverse sequence)
  (fold-left
   (lambda (x y) ⟨??⟩) nil sequence))
```

### Các Ánh Xạ Lồng Nhau

Chúng ta có thể mở rộng mô hình chuỗi để bao gồm nhiều tính toán thường được biểu thị bằng các vòng lặp lồng nhau.^[Cách tiếp cận các ánh xạ lồng nhau này được David Turner chỉ cho chúng ta, người có các ngôn ngữ KRC và Miranda cung cấp các hình thức trang nhã để xử lý các cấu trúc này. Các ví dụ trong phần này (xem thêm [Bài tập 2.42](#Exercise-2_002e42)) được điều chỉnh từ [Turner 1981](References.xhtml#Turner-1981). Trong [3.5.3](3_002e5.xhtml#g_t3_002e5_002e3), chúng ta sẽ thấy cách cách tiếp cận này tổng quát hóa thành các chuỗi vô hạn.] Hãy xem xét vấn đề này: Cho một số nguyên dương $n$, hãy tìm tất cả các cặp số nguyên dương riêng biệt có thứ tự $i$ và $j$, trong đó ${1 \leq j} < {i \leq n}$, sao cho $i + j$ là số nguyên tố. Ví dụ: nếu $n$ là 6, thì các cặp là như sau:

$$\begin{array}{llllllll}
i & 2 & 3 & 4 & 4 & 5 & 6 & 6 \\
j & 1 & 2 & 1 & 3 & 2 & 1 & 5 \\
{i + j} & 3 & 5 & 5 & 7 & 7 & 7 & 11 \\
\end{array}$$

Một cách tự nhiên để tổ chức tính toán này là tạo chuỗi tất cả các cặp số nguyên dương có thứ tự nhỏ hơn hoặc bằng $n$, lọc để chọn những cặp có tổng là số nguyên tố, và sau đó, đối với mỗi cặp $(i,j)$ vượt qua bộ lọc, tạo ra bộ ba $(i,j,i + j)$.

Đây là cách tạo chuỗi các cặp: Đối với mỗi số nguyên $i \leq n$, hãy liệt kê các số nguyên $j < i$ và đối với mỗi $i$ và $j$ như vậy, hãy tạo cặp $(i,j)$. Theo các phép toán chuỗi, chúng ta ánh xạ dọc theo chuỗi `(enumerate-interval 1 n)`. Đối với mỗi $i$ trong chuỗi này, chúng ta ánh xạ dọc theo chuỗi `(enumerate-interval 1 (- i 1))`. Đối với mỗi $j$ trong chuỗi sau, chúng ta tạo cặp `(list i j)`. Điều này cung cấp cho chúng ta một chuỗi các cặp cho mỗi $i$. Kết hợp tất cả các chuỗi cho tất cả các $i$ (bằng cách tích lũy với `append`) sẽ tạo ra chuỗi các cặp yêu cầu:^[Ở đây chúng ta đang biểu diễn một cặp dưới dạng một danh sách gồm hai phần tử thay vì một cặp Lisp. Do đó, "cặp" $(i,j)$ được biểu diễn là `(list i j)`, không phải `(cons i j)`.]

```scheme
(accumulate
 append
 nil
 (map (lambda (i)
        (map (lambda (j)
               (list i j))
             (enumerate-interval 1 (- i 1))))
      (enumerate-interval 1 n)))
```

Sự kết hợp giữa ánh xạ và tích lũy với `append` rất phổ biến trong loại chương trình này nên chúng ta sẽ cô lập nó như một thủ tục riêng biệt:

```scheme
(define (flatmap proc seq)
  (accumulate append nil (map proc seq)))
```

Bây giờ, hãy lọc chuỗi các cặp này để tìm những cặp có tổng là số nguyên tố. Vị từ bộ lọc được gọi cho mỗi phần tử của chuỗi; đối số của nó là một cặp và nó phải trích xuất các số nguyên từ cặp. Do đó, vị từ áp dụng cho mỗi phần tử trong chuỗi là

```scheme
(define (prime-sum? pair)
  (prime? (+ (car pair) (cadr pair))))
```

Cuối cùng, hãy tạo chuỗi kết quả bằng cách ánh xạ trên các cặp đã lọc bằng cách sử dụng thủ tục sau, thủ tục này tạo một bộ ba bao gồm hai phần tử của cặp cùng với tổng của chúng:

```scheme
(define (make-pair-sum pair)
  (list (car pair)
        (cadr pair)
        (+ (car pair) (cadr pair))))
```

Kết hợp tất cả các bước này sẽ cho ra thủ tục hoàn chỉnh:

```scheme
(define (prime-sum-pairs n)
  (map make-pair-sum
       (filter
        prime-sum?
        (flatmap
         (lambda (i)
           (map (lambda (j)
                  (list i j))
                (enumerate-interval
                 1
                 (- i 1))))
         (enumerate-interval 1 n)))))
```

Các ánh xạ lồng nhau cũng hữu ích cho các chuỗi khác với các chuỗi liệt kê các khoảng. Giả sử chúng ta muốn tạo ra tất cả các hoán vị của một tập hợp $S$; tức là, tất cả các cách sắp xếp các mục trong tập hợp. Ví dụ: các hoán vị của $\{ 1,2,3\}$ là $\{ 1,2,3\}$, $\{ 1,3,2\}$, $\{ 2,1,3\}$, $\{ 2,3,1\}$, $\{ 3,1,2\}$ và $\{ 3,2,1\}$. Đây là một kế hoạch để tạo các hoán vị của $S$: Đối với mỗi mục $x$ trong $S$, hãy tạo đệ quy chuỗi các hoán vị của $S - x$,^[Tập hợp $S - x$ là tập hợp tất cả các phần tử của $S$, loại trừ $x$.] và nối $x$ vào đầu mỗi hoán vị. Điều này tạo ra, cho mỗi $x$ trong $S$, chuỗi các hoán vị của $S$ bắt đầu bằng $x$. Kết hợp các chuỗi này cho tất cả các $x$ sẽ cho tất cả các hoán vị của $S$:^[Dấu chấm phẩy trong mã Scheme được sử dụng để giới thiệu *nhận xét*. Mọi thứ từ dấu chấm phẩy đến cuối dòng đều bị trình thông dịch bỏ qua. Trong cuốn sách này, chúng tôi không sử dụng nhiều nhận xét; chúng tôi cố gắng làm cho các chương trình của mình tự tài liệu bằng cách sử dụng các tên mô tả.]

```scheme
(define (permutations s)
  (if (null? s)   ; tập hợp rỗng?
      (list nil)  ; chuỗi chứa tập hợp rỗng
      (flatmap (lambda (x)
                 (map (lambda (p)
                        (cons x p))
                      (permutations
                       (remove x s))))
               s)))
```

Lưu ý cách chiến lược này giảm vấn đề tạo các hoán vị của $S$ thành vấn đề tạo các hoán vị của các tập hợp có ít phần tử hơn $S$. Trong trường hợp kết thúc, chúng ta tìm đường đi xuống đến danh sách rỗng, biểu thị một tập hợp không có phần tử. Đối với điều này, chúng ta tạo `(list nil)`, đây là một chuỗi có một mục, cụ thể là tập hợp không có phần tử. Thủ tục `remove` được sử dụng trong `permutations` trả về tất cả các mục trong một chuỗi đã cho ngoại trừ một mục đã cho. Điều này có thể được biểu thị như một bộ lọc đơn giản:

```scheme
(define (remove item sequence)
  (filter (lambda (x) (not (= x item)))
          sequence))
```

**Bài tập 2.40:** Hãy định nghĩa một thủ tục `unique-pairs` mà, cho một số nguyên $n$, tạo ra chuỗi các cặp $(i,j)$ với ${1 \leq j} < {i \leq n}$. Sử dụng `unique-pairs` để đơn giản hóa định nghĩa của `prime-sum-pairs` đã cho ở trên.

**Bài tập 2.41:** Viết một thủ tục để tìm tất cả các bộ ba số nguyên dương riêng biệt có thứ tự $i$, $j$ và $k$ nhỏ hơn hoặc bằng một số nguyên $n$ đã cho mà có tổng bằng một số nguyên $s$ đã cho.

**Bài tập 2.42:** "Bài toán tám quân hậu" hỏi làm thế nào để đặt tám quân hậu trên một bàn cờ sao cho không có quân hậu nào bị chiếu bởi bất kỳ quân hậu nào khác (tức là, không có hai quân hậu nào ở cùng một hàng, cột hoặc đường chéo). Một giải pháp khả thi được hiển thị trong [Hình 2.8](#Figure-2_002e8). Một cách để giải bài toán là làm việc trên bàn cờ, đặt một quân hậu vào mỗi cột. Khi chúng ta đã đặt $k - 1$ quân hậu, chúng ta phải đặt quân hậu thứ $k$ vào một vị trí mà nó không chiếu bất kỳ quân hậu nào đã có trên bàn cờ. Chúng ta có thể xây dựng cách tiếp cận này một cách đệ quy: Giả sử rằng chúng ta đã tạo chuỗi tất cả các cách có thể để đặt $k - 1$ quân hậu trong $k - 1$ cột đầu tiên của bàn cờ. Đối với mỗi cách này, hãy tạo một tập hợp các vị trí mở rộng bằng cách đặt một quân hậu vào mỗi hàng của cột thứ $k$. Bây giờ, hãy lọc những vị trí này, chỉ giữ lại các vị trí mà quân hậu ở cột thứ $k$ an toàn so với các quân hậu khác. Điều này tạo ra chuỗi tất cả các cách để đặt $k$ quân hậu trong $k$ cột đầu tiên. Bằng cách tiếp tục quá trình này, chúng ta sẽ tạo ra không chỉ một giải pháp mà là tất cả các giải pháp cho bài toán.

![](fig/chap2/Fig2.8c.std.svg 400.92x400.92)

SVG

**Hình 2.8:** Một giải pháp cho bài toán tám quân hậu.

Chúng ta triển khai giải pháp này như một thủ tục `queens`, trả về một chuỗi tất cả các giải pháp cho bài toán đặt $n$ quân hậu trên bàn cờ $n \times n$. `Queens` có một thủ tục nội bộ `queen-cols` trả về chuỗi tất cả các cách đặt quân hậu trong $k$ cột đầu tiên của bàn cờ.

```scheme
(define (queens board-size)
  (define (queen-cols k)
    (if (= k 0)
        (list empty-board)
        (filter
         (lambda (positions)
           (safe? k positions))
         (flatmap
          (lambda (rest-of-queens)
            (map (lambda (new-row)
                   (adjoin-position
                    new-row
                    k
                    rest-of-queens))
                 (enumerate-interval
                  1
                  board-size)))
          (queen-cols (- k 1))))))
  (queen-cols board-size))
```

Trong thủ tục này, `rest-of-queens` là một cách để đặt $k - 1$ quân hậu trong $k - 1$ cột đầu tiên và `new-row` là một hàng được đề xuất để đặt quân hậu cho cột thứ $k$. Hoàn thành chương trình bằng cách triển khai biểu diễn cho các tập hợp các vị trí trên bàn cờ, bao gồm cả thủ tục `adjoin-position`, nối một vị trí hàng-cột mới vào một tập hợp các vị trí và `empty-board`, đại diện cho một tập hợp các vị trí rỗng. Bạn cũng phải viết thủ tục `safe?`, xác định cho một tập hợp các vị trí, liệu quân hậu ở cột thứ $k$ có an toàn so với các quân hậu khác hay không. (Lưu ý rằng chúng ta chỉ cần kiểm tra xem quân hậu mới có an toàn hay không—các quân hậu khác đã được đảm bảo an toàn so với nhau).

**Bài tập 2.43:** Louis Reasoner đang gặp khó khăn trong khi thực hiện [Bài tập 2.42](#Exercise-2_002e42). Thủ tục `queens` của anh ấy dường như hoạt động, nhưng nó chạy cực kỳ chậm. (Louis không bao giờ có thể chờ đủ lâu để nó giải được ngay cả trường hợp $6 \times 6$.) Khi Louis hỏi Eva Lu Ator để được giúp đỡ, cô ấy chỉ ra rằng anh ấy đã hoán đổi thứ tự của các ánh xạ lồng nhau trong `flatmap`, viết nó như sau

```scheme
(flatmap
 (lambda (new-row)
   (map (lambda (rest-of-queens)
          (adjoin-position
           new-row k rest-of-queens))
        (queen-cols (- k 1))))
 (enumerate-interval 1 board-size))
```

Hãy giải thích tại sao việc hoán đổi này làm cho chương trình chạy chậm. Hãy ước tính thời gian chương trình của Louis sẽ mất để giải bài toán tám quân hậu, giả sử rằng chương trình trong [Bài tập 2.42](#Exercise-2_002e42) giải bài toán trong thời gian $T$.

## 2.2.4 Ví dụ: Ngôn Ngữ Hình Ảnh

Phần này trình bày một ngôn ngữ đơn giản để vẽ hình minh họa sức mạnh của trừu tượng hóa dữ liệu và tính chất đóng, đồng thời khai thác các thủ tục bậc cao một cách thiết yếu. Ngôn ngữ này được thiết kế để giúp bạn dễ dàng thử nghiệm các mẫu như trong [Hình 2.9](#Figure-2_002e9), được cấu tạo từ các phần tử lặp đi lặp lại được dịch chuyển và chia tỷ lệ.^[Ngôn ngữ hình ảnh dựa trên ngôn ngữ Peter Henderson đã tạo ra để xây dựng các hình ảnh như bản khắc gỗ "Square Limit" của M.C. Escher (xem [Henderson 1982](References.xhtml#Henderson-1982)). Bản khắc gỗ kết hợp một mẫu tỷ lệ lặp lại, tương tự như các cách sắp xếp được vẽ bằng cách sử dụng thủ tục `square-limit` trong phần này.] Trong ngôn ngữ này, các đối tượng dữ liệu đang được kết hợp được biểu diễn dưới dạng các thủ tục chứ không phải là cấu trúc danh sách. Giống như `cons`, thỏa mãn tính chất đóng, cho phép chúng ta dễ dàng xây dựng cấu trúc danh sách phức tạp tùy ý, các phép toán trong ngôn ngữ này, cũng thỏa mãn tính chất đóng, cho phép chúng ta dễ dàng xây dựng các mẫu phức tạp tùy ý.

![](fig/chap2/Fig2.9.std.svg 670.32x376.08)
**Hình 2.9:** Các thiết kế được tạo ra bằng ngôn ngữ hình ảnh.

### Ngôn Ngữ Hình Ảnh

Khi bắt đầu nghiên cứu về lập trình trong [1.1](1_002e1.xhtml#g_t1_002e1), chúng ta đã nhấn mạnh tầm quan trọng của việc mô tả một ngôn ngữ bằng cách tập trung vào các nguyên thủy của ngôn ngữ, các phương tiện kết hợp và các phương tiện trừu tượng hóa. Chúng ta sẽ tuân theo khuôn khổ đó ở đây.

Một phần của sự thanh lịch của ngôn ngữ hình ảnh này là chỉ có một loại phần tử, được gọi là *họa sĩ*. Một họa sĩ vẽ một hình ảnh được dịch chuyển và chia tỷ lệ để vừa với một khung hình dạng hình bình hành được chỉ định. Ví dụ: có một họa sĩ nguyên thủy mà chúng ta sẽ gọi là `wave` tạo ra một bản vẽ đường nét thô, như được hiển thị trong [Hình 2.10](#Figure-2_002e10). Hình dạng thực tế của bản vẽ phụ thuộc vào khung—cả bốn hình ảnh trong Hình 2.10 đều được tạo ra bởi cùng một họa sĩ `wave`, nhưng liên quan đến bốn khung khác nhau. Các họa sĩ có thể phức tạp hơn thế này: Họa sĩ nguyên thủy có tên `rogers` vẽ một bức tranh về người sáng lập MIT, William Barton Rogers, như được hiển thị trong [Hình 2.11](#Figure-2_002e11).^[William Barton Rogers (1804-1882) là người sáng lập và là chủ tịch đầu tiên của MIT. Một nhà địa chất học và giáo viên tài năng, ông đã dạy tại William and Mary College và tại Đại học Virginia. Năm 1859, ông chuyển đến Boston, nơi ông có nhiều thời gian hơn cho nghiên cứu, làm việc về kế hoạch thành lập "viện bách khoa" và giữ chức vụ Thanh tra Máy đo Khí đốt đầu tiên của bang Massachusetts.] Bốn hình ảnh trong Hình 2.11 được vẽ liên quan đến cùng bốn khung như các hình ảnh `wave` trong Hình 2.10.

![](fig/chap2/Fig2.10.std.svg 338.76x362.64)
**Hình 2.10:** Các hình ảnh được tạo bởi họa sĩ `wave`, liên quan đến bốn khung khác nhau. Các khung, được hiển thị bằng các đường chấm chấm, không phải là một phần của hình ảnh.

![](fig/chap2/Fig2.11.std.svg 338.76x375.12)
**Hình 2.11:** Các hình ảnh của William Barton Rogers, người sáng lập và là chủ tịch đầu tiên của MIT, được vẽ liên quan đến cùng bốn khung như trong [Hình 2.10](#Figure-2_002e10) (hình ảnh gốc từ Wikimedia Commons).

Để kết hợp các hình ảnh, chúng ta sử dụng các phép toán khác nhau tạo ra các họa sĩ mới từ các họa sĩ đã cho. Ví dụ: phép toán `beside` nhận hai họa sĩ và tạo ra một họa sĩ phức hợp mới, vẽ hình ảnh của họa sĩ đầu tiên ở nửa bên trái của khung và hình ảnh của họa sĩ thứ hai ở nửa bên phải của khung. Tương tự, `below` nhận hai họa sĩ và tạo ra một họa sĩ phức hợp, vẽ hình ảnh của họa sĩ đầu tiên bên dưới hình ảnh của họa sĩ thứ hai. Một số phép toán biến đổi một họa sĩ duy nhất để tạo ra một họa sĩ mới. Ví dụ, `flip-vert` nhận một họa sĩ và tạo ra một họa sĩ vẽ hình ảnh của nó lộn ngược và `flip-horiz` tạo ra một họa sĩ vẽ hình ảnh của họa sĩ gốc bị đảo ngược từ trái sang phải.

[Hình 2.12](#Figure-2_002e12) cho thấy bản vẽ của một họa sĩ có tên là `wave4` được xây dựng qua hai giai đoạn bắt đầu từ `wave`:

```scheme
(define wave2 (beside wave (flip-vert wave)))
(define wave4 (below wave2 wave2))
```

![](fig/chap2/Fig2.12.std.svg 564.72x312.84)
**Hình 2.12:** Tạo một hình phức tạp, bắt đầu từ họa sĩ `wave` của [Hình 2.10](#Figure-2_002e10).

Khi xây dựng một hình ảnh phức tạp theo cách này, chúng ta đang khai thác thực tế là các họa sĩ được đóng theo các phương tiện kết hợp của ngôn ngữ. `beside` hoặc `below` của hai họa sĩ bản thân nó là một họa sĩ; do đó, chúng ta có thể sử dụng nó như một phần tử để tạo ra các họa sĩ phức tạp hơn. Cũng như việc xây dựng cấu trúc danh sách bằng cách sử dụng `cons`, tính chất đóng của dữ liệu theo các phương tiện kết hợp là rất quan trọng đối với khả năng tạo ra các cấu trúc phức tạp trong khi chỉ sử dụng một số ít các phép toán.

Khi chúng ta có thể kết hợp các họa sĩ, chúng ta muốn có thể trừu tượng hóa các mẫu điển hình của việc kết hợp các họa sĩ. Chúng ta sẽ triển khai các phép toán của họa sĩ dưới dạng các thủ tục Scheme. Điều này có nghĩa là chúng ta không cần một cơ chế trừu tượng đặc biệt trong ngôn ngữ hình ảnh: Vì các phương tiện kết hợp là các thủ tục Scheme thông thường, nên chúng ta tự động có khả năng thực hiện bất kỳ điều gì với các phép toán của họa sĩ mà chúng ta có thể thực hiện với các thủ tục. Ví dụ: chúng ta có thể trừu tượng hóa mẫu trong `wave4` là

```scheme
(define (flipped-pairs painter)
  (let ((painter2
         (beside painter
                 (flip-vert painter))))
    (below painter2 painter2)))
```

và định nghĩa `wave4` là một thể hiện của mẫu này:

```scheme
(define wave4 (flipped-pairs wave))
```

Chúng ta cũng có thể định nghĩa các phép toán đệ quy. Đây là một phép toán tạo ra các họa sĩ tách và phân nhánh sang bên phải như được hiển thị trong [Hình 2.13](#Figure-2_002e13) và [Hình 2.14](#Figure-2_002e14):

```scheme
(define (right-split painter n)
  (if (= n 0)
      painter
      (let ((smaller (right-split painter
                                  (- n 1))))
        (beside painter
                (below smaller smaller)))))
```

![](fig/chap2/Fig2.13a.std.svg 625.8x826.8)
**Hình 2.13:** Các kế hoạch đệ quy cho `right-split` và `corner-split`.

Chúng ta có thể tạo ra các mẫu cân bằng bằng cách phân nhánh lên trên cũng như sang bên phải (xem [Bài tập 2.44](#Exercise-2_002e44), [Hình 2.13](#Figure-2_002e13) và [Hình 2.14](#Figure-2_002e14)):

```scheme
(define (corner-split painter n)
  (if (= n 0)
      painter
      (let ((up (up-split painter (- n 1)))
            (right (right-split painter
                                (- n 1))))
        (let ((top-left (beside up up))
              (bottom-right (below right
                                   right))
              (corner (corner-split painter
                                    (- n 1))))
          (beside (below painter top-left)
                  (below bottom-right
                         corner))))))
```

![](fig/chap2/Fig2.14b.std.svg 635.16x747.0)
**Hình 2.14:** Các phép toán đệ quy `right-split` và `corner-split` được áp dụng cho các họa sĩ `wave` và `rogers`. Việc kết hợp bốn hình `corner-split` tạo ra các thiết kế `square-limit` đối xứng như được hiển thị trong [Hình 2.9](#Figure-2_002e9).

Bằng cách đặt bốn bản sao của một `corner-split` một cách thích hợp, chúng ta có được một mẫu gọi là `square-limit`, mà ứng dụng của nó cho `wave` và `rogers` được hiển thị trong [Hình 2.9](#Figure-2_002e9):

```scheme
(define (square-limit painter n)
  (let ((quarter (corner-split painter n)))
    (let ((half (beside (flip-horiz quarter)
                        quarter)))
      (below (flip-vert half) half))))
```

**Bài tập 2.44:** Hãy định nghĩa thủ tục `up-split` được sử dụng bởi `corner-split`. Nó tương tự như `right-split`, ngoại trừ việc nó chuyển đổi vai trò của `below` và `beside`.

### Các Phép Toán Bậc Cao

Ngoài việc trừu tượng hóa các mẫu kết hợp họa sĩ, chúng ta có thể làm việc ở cấp độ cao hơn, trừu tượng hóa các mẫu kết hợp các phép toán của họa sĩ. Tức là, chúng ta có thể xem các phép toán của họa sĩ như các phần tử để thao tác và có thể viết các phương tiện kết hợp cho các phần tử này—các thủ tục nhận các phép toán của họa sĩ làm đối số và tạo ra các phép toán của họa sĩ mới.

Ví dụ: `flipped-pairs` và `square-limit` mỗi cái sắp xếp bốn bản sao của hình ảnh của họa sĩ theo một mẫu hình vuông; chúng chỉ khác nhau ở cách chúng định hướng các bản sao. Một cách để trừu tượng hóa mẫu kết hợp họa sĩ này là với thủ tục sau, thủ tục này nhận bốn phép toán của họa sĩ một đối số và tạo ra một phép toán của họa sĩ biến đổi một họa sĩ đã cho bằng bốn phép toán đó và sắp xếp các kết quả theo một hình vuông. `Tl`, `tr`, `bl` và `br` lần lượt là các phép biến đổi để áp dụng cho bản sao trên cùng bên trái, bản sao trên cùng bên phải, bản sao dưới cùng bên trái và bản sao dưới cùng bên phải.

```scheme
(define (square-of-four tl tr bl br)
  (lambda (painter)
    (let ((top (beside (tl painter)
                       (tr painter)))
          (bottom (beside (bl painter)
                          (br painter))))
      (below bottom top))))
```

Sau đó, `flipped-pairs` có thể được định nghĩa theo `square-of-four` như sau:^[Tương đương, chúng ta có thể viết]

```scheme
(define (flipped-pairs painter)
  (let ((combine4
         (square-of-four identity
                         flip-vert
                         identity
                         flip-vert)))
    (combine4 painter)))
```

và `square-limit` có thể được biểu thị là^[`Rotate180` xoay một họa sĩ 180 độ (xem [Bài tập 2.50](#Exercise-2_002e50)). Thay vì `rotate180`, chúng ta có thể nói `(compose flip-vert flip-horiz)`, bằng cách sử dụng thủ tục `compose` từ [Bài tập 1.42](1_002e3.xhtml#Exercise-1_002e42).]

```scheme
(define (square-limit painter n)
  (let ((combine4
         (square-of-four flip-horiz
                         identity
                         rotate180
                         flip-vert)))
    (combine4 (corner-split painter n))))
```

**Bài tập 2.45:** `Right-split` và `up-split` có thể được biểu thị dưới dạng các thể hiện của một phép toán tách chung. Hãy định nghĩa một thủ tục `split` có thuộc tính là đánh giá

```scheme
(define right-split (split beside below))
(define up-split (split below beside))
```

tạo ra các thủ tục `right-split` và `up-split` có cùng hành vi như những thủ tục đã được định nghĩa.

### Các Khung

Trước khi chúng ta có thể chỉ ra cách triển khai các họa sĩ và phương tiện kết hợp của chúng, trước tiên chúng ta phải xem xét các khung. Một khung có thể được mô tả bởi ba vectơ—một vectơ gốc và hai vectơ cạnh. Vectơ gốc chỉ định độ lệch của gốc khung so với một gốc tuyệt đối nào đó trên mặt phẳng và các vectơ cạnh chỉ định độ lệch của các góc khung so với gốc của nó. Nếu các cạnh vuông góc, khung sẽ là hình chữ nhật. Nếu không, khung sẽ là một hình bình hành tổng quát hơn.

[Hình 2.15](#Figure-2_002e15) cho thấy một khung và các vectơ liên quan của nó. Theo trừu tượng hóa dữ liệu, chúng ta chưa cần phải cụ thể về cách các khung được biểu diễn, ngoài việc nói rằng có một bộ xây dựng `make-frame`, nhận ba vectơ và tạo ra một khung, và ba bộ chọn tương ứng `origin-frame`, `edge1-frame` và `edge2-frame` (xem [Bài tập 2.47](#Exercise-2_002e47)).

![](fig/chap2/Fig2.15a.std.svg 408.24x384.36)
**Hình 2.15:** Một khung được mô tả bởi ba vectơ — một gốc và hai cạnh.

Chúng ta sẽ sử dụng các tọa độ trong hình vuông đơn vị $(0 \leq x,y \leq 1)$ để chỉ định hình ảnh. Với mỗi khung, chúng ta liên kết một *ánh xạ tọa độ khung*, sẽ được sử dụng để dịch chuyển và chia tỷ lệ hình ảnh cho vừa với khung. Ánh xạ biến đổi hình vuông đơn vị thành khung bằng cách ánh xạ vectơ $\mathbf{v} = (x,y)$ thành tổng vectơ

$$\text{Gốc(Khung)} + {x \cdot \text{Cạnh}_{1}\text{(Khung)}} + {y \cdot \text{Cạnh}_{2}\text{(Khung)}.}$$

Ví dụ: (0, 0) được ánh xạ vào gốc của khung, (1, 1) vào đỉnh đối diện theo đường chéo với gốc và (0,5, 0,5) vào tâm của khung. Chúng ta có thể tạo bản đồ tọa độ của khung bằng thủ tục sau:^[`Frame-coord-map` sử dụng các phép toán vectơ được mô tả trong [Bài tập 2.46](#Exercise-2_002e46) bên dưới, mà chúng ta giả định đã được triển khai bằng cách sử dụng một số biểu diễn cho các vectơ. Do trừu tượng hóa dữ liệu, không quan trọng biểu diễn vectơ này là gì, miễn là các phép toán vectơ hoạt động chính xác.]

```scheme
(define (frame-coord-map frame)
  (lambda (v)
    (add-vect
     (origin-frame frame)
     (add-vect
      (scale-vect (xcor-vect v)
                  (edge1-frame frame))
      (scale-vect (ycor-vect v)
                  (edge2-frame frame))))))
```

Quan sát rằng việc áp dụng `frame-coord-map` cho một khung sẽ trả về một thủ tục mà, khi nhận một vectơ, sẽ trả về một vectơ. Nếu vectơ đối số nằm trong hình vuông đơn vị, vectơ kết quả sẽ nằm trong khung. Ví dụ,

```scheme
((frame-coord-map a-frame) (make-vect 0 0))
```

trả về cùng một vectơ với

```scheme
(origin-frame a-frame)
```

**Bài tập 2.46:** Một vectơ hai chiều $\mathbf{v}$ chạy từ gốc đến một điểm có thể được biểu diễn dưới dạng một cặp bao gồm tọa độ $x$ và tọa độ $y$. Hãy triển khai một trừu tượng hóa dữ liệu cho các vectơ bằng cách đưa ra một bộ xây dựng `make-vect` và các bộ chọn tương ứng `xcor-vect` và `ycor-vect`. Theo các bộ chọn và bộ xây dựng của bạn, hãy triển khai các thủ tục `add-vect`, `sub-vect` và `scale-vect` thực hiện các phép toán cộng vectơ, trừ vectơ và nhân một vectơ với một vô hướng:

$$\begin{array}{lll}
{(x_{1},y_{1}) + (x_{2},y_{2})} & = & {(x_{1} + x_{2},y_{1} + y_{2}),} \\
{(x_{1},y_{1}) - (x_{2},y_{2})} & = & {(x_{1} - x_{2},y_{1} - y_{2}),} \\
{s \cdot (x,y)} & = & {(sx,sy).} \\
\end{array}$$

**Bài tập 2.47:** Đây là hai bộ xây dựng có thể có cho khung:

```scheme
(define (make-frame origin edge1 edge2)
  (list origin edge1 edge2))

(define (make-frame origin edge1 edge2)
  (cons origin (cons edge1 edge2)))
```

Đối với mỗi bộ xây dựng, hãy cung cấp các bộ chọn thích hợp để tạo ra một triển khai cho khung.

### Họa Sĩ

Một họa sĩ được biểu diễn dưới dạng một thủ tục mà, khi nhận một khung làm đối số, sẽ vẽ một hình ảnh cụ thể được dịch chuyển và chia tỷ lệ cho vừa với khung. Tức là, nếu `p` là một họa sĩ và `f` là một khung, thì chúng ta tạo ra hình ảnh của `p` trong `f` bằng cách gọi `p` với `f` làm đối số.

Các chi tiết về cách các họa sĩ nguyên thủy được triển khai phụ thuộc vào các đặc điểm cụ thể của hệ thống đồ họa và loại hình ảnh sẽ được vẽ. Ví dụ: giả sử chúng ta có một thủ tục `draw-line` vẽ một đường thẳng trên màn hình giữa hai điểm được chỉ định. Sau đó, chúng ta có thể tạo ra các họa sĩ cho các bản vẽ đường nét, chẳng hạn như họa sĩ `wave` trong [Hình 2.10](#Figure-2_002e10), từ danh sách các đoạn đường thẳng như sau:^[`Segments->painter` sử dụng biểu diễn cho các đoạn đường thẳng được mô tả trong [Bài tập 2.48](#Exercise-2_002e48) bên dưới. Nó cũng sử dụng thủ tục `for-each` được mô tả trong [Bài tập 2.23](#Exercise-2_002e23).]

```scheme
(define (segments->painter segment-list)
  (lambda (frame)
    (for-each
     (lambda (segment)
       (draw-line
        ((frame-coord-map frame)
         (start-segment segment))
        ((frame-coord-map frame)
         (end-segment segment))))
     segment-list)))
```

Các đoạn được đưa ra bằng cách sử dụng các tọa độ liên quan đến hình vuông đơn vị. Đối với mỗi đoạn trong danh sách, họa sĩ biến đổi các điểm cuối của đoạn bằng ánh xạ tọa độ khung và vẽ một đường thẳng giữa các điểm đã biến đổi.

Việc biểu diễn các họa sĩ dưới dạng các thủ tục dựng lên một rào cản trừu tượng mạnh mẽ trong ngôn ngữ hình ảnh. Chúng ta có thể tạo và trộn lẫn tất cả các loại họa sĩ nguyên thủy, dựa trên nhiều khả năng đồ họa khác nhau. Các chi tiết về việc triển khai chúng không quan trọng. Bất kỳ thủ tục nào cũng có thể đóng vai trò là một họa sĩ, miễn là nó nhận một khung làm đối số và vẽ một cái gì đó được chia tỷ lệ cho vừa với khung.^[Ví dụ: họa sĩ `rogers` trong [Hình 2.11](#Figure-2_002e11) được xây dựng từ một hình ảnh mức độ xám. Đối với mỗi điểm trong một khung đã cho, họa sĩ `rogers` xác định điểm trong hình ảnh được ánh xạ tới nó theo ánh xạ tọa độ khung và tô bóng nó cho phù hợp. Bằng cách cho phép các loại họa sĩ khác nhau, chúng ta đang tận dụng ý tưởng dữ liệu trừu tượng được thảo luận trong [2.1.3](2_002e1.xhtml#g_t2_002e1_002e3), nơi chúng ta lập luận rằng biểu diễn số hữu tỉ có thể là bất cứ điều gì đáp ứng một điều kiện thích hợp. Ở đây chúng ta đang sử dụng thực tế là một họa sĩ có thể được triển khai theo bất kỳ cách nào, miễn là nó vẽ một cái gì đó trong khung được chỉ định. [2.1.3](2_002e1.xhtml#g_t2_002e1_002e3) cũng chỉ ra cách các cặp có thể được triển khai dưới dạng các thủ tục. Các họa sĩ là ví dụ thứ hai của chúng ta về biểu diễn thủ tục cho dữ liệu.]

**Bài tập 2.48:** Một đoạn thẳng có hướng trên mặt phẳng có thể được biểu diễn dưới dạng một cặp vectơ—vectơ chạy từ gốc đến điểm bắt đầu của đoạn và vectơ chạy từ gốc đến điểm kết thúc của đoạn. Sử dụng biểu diễn vectơ của bạn từ [Bài tập 2.46](#Exercise-2_002e46) để xác định một biểu diễn cho các đoạn với bộ xây dựng `make-segment` và các bộ chọn `start-segment` và `end-segment`.

**Bài tập 2.49:** Sử dụng `segments->painter` để định nghĩa các họa sĩ nguyên thủy sau:

1. Họa sĩ vẽ đường viền của khung được chỉ định.
2. Họa sĩ vẽ chữ "X" bằng cách nối các góc đối diện của khung.
3. Họa sĩ vẽ hình kim cương bằng cách nối các trung điểm của các cạnh của khung.
4. Họa sĩ `wave`.

### Biến đổi và kết hợp các họa sĩ

Một phép toán trên các họa sĩ (chẳng hạn như `flip-vert` hoặc `beside`) hoạt động bằng cách tạo ra một họa sĩ gọi các họa sĩ gốc liên quan đến các khung được tạo từ khung đối số. Do đó, ví dụ: `flip-vert` không cần phải biết cách một họa sĩ hoạt động để lật nó—nó chỉ cần biết cách lật ngược một khung: Họa sĩ đã lật chỉ sử dụng họa sĩ gốc, nhưng trong khung bị đảo ngược.

Các phép toán của họa sĩ dựa trên thủ tục `transform-painter`, nhận các đối số là một họa sĩ và thông tin về cách biến đổi một khung và tạo ra một họa sĩ mới. Họa sĩ đã biến đổi, khi được gọi trên một khung, sẽ biến đổi khung và gọi họa sĩ gốc trên khung đã biến đổi. Các đối số cho `transform-painter` là các điểm (được biểu diễn dưới dạng vectơ) chỉ định các góc của khung mới: Khi được ánh xạ vào khung, điểm đầu tiên chỉ định gốc của khung mới và hai điểm còn lại chỉ định các điểm cuối của các vectơ cạnh của nó. Do đó, các đối số trong hình vuông đơn vị chỉ định một khung nằm trong khung gốc.

```scheme
(define (transform-painter
         painter origin corner1 corner2)
  (lambda (frame)
    (let ((m (frame-coord-map frame)))
      (let ((new-origin (m origin)))
        (painter (make-frame new-origin
                  (sub-vect (m corner1)
                            new-origin)
                  (sub-vect (m corner2)
                            new-origin)))))))
```

Đây là cách lật các hình ảnh của họa sĩ theo chiều dọc:

```scheme
(define (flip-vert painter)
  (transform-painter
   painter
   (make-vect 0.0 1.0)   ; gốc mới
   (make-vect 1.0 1.0)   ; đầu mới của cạnh 1
   (make-vect 0.0 0.0))) ; đầu mới của cạnh 2
```

Sử dụng `transform-painter`, chúng ta có thể dễ dàng định nghĩa các phép biến đổi mới. Ví dụ: chúng ta có thể định nghĩa một họa sĩ thu nhỏ hình ảnh của nó xuống phần tư phía trên bên phải của khung mà nó được cung cấp:

```scheme
(define (shrink-to-upper-right painter)
  (transform-painter painter
                     (make-vect 0.5 0.5)
                     (make-vect 1.0 0.5)
                     (make-vect 0.5 1.0)))
```

Các phép biến đổi khác xoay hình ảnh ngược chiều kim đồng hồ 90 độ^[`Rotate90` chỉ là một phép quay thuần túy đối với các khung hình vuông, vì nó cũng kéo dài và thu nhỏ hình ảnh cho vừa với khung đã xoay.]

```scheme
(define (rotate90 painter)
  (transform-painter painter
                     (make-vect 1.0 0.0)
                     (make-vect 1.0 1.0)
                     (make-vect 0.0 0.0)))
```

hoặc ép hình ảnh vào tâm khung:^[Các hình ảnh hình kim cương trong [Hình 2.10](#Figure-2_002e10) và [Hình 2.11](#Figure-2_002e11) được tạo bằng cách áp dụng `squash-inwards` cho `wave` và `rogers`.]

```scheme
(define (squash-inwards painter)
  (transform-painter painter
                     (make-vect 0.0 0.0)
                     (make-vect 0.65 0.35)
                     (make-vect 0.35 0.65)))
```

Biến đổi khung cũng là chìa khóa để định nghĩa các phương tiện kết hợp hai hoặc nhiều họa sĩ. Ví dụ: thủ tục `beside` nhận hai họa sĩ, biến đổi chúng để vẽ tương ứng ở nửa bên trái và bên phải của một khung đối số, đồng thời tạo ra một họa sĩ phức hợp mới. Khi họa sĩ phức hợp được cung cấp một khung, nó sẽ gọi họa sĩ đã biến đổi đầu tiên để vẽ ở nửa bên trái của khung và gọi họa sĩ đã biến đổi thứ hai để vẽ ở nửa bên phải của khung:

```scheme
(define (beside painter1 painter2)
  (let ((split-point (make-vect 0.5 0.0)))
    (let ((paint-left  (transform-painter
                        painter1
                        (make-vect 0.0 0.0)
                        split-point
                        (make-vect 0.0 1.0)))
          (paint-right (transform-painter
                        painter2
                        split-point
                        (make-vect 1.0 0.0)
                        (make-vect 0.5 1.0))))
      (lambda (frame)
        (paint-left frame)
        (paint-right frame)))))
```

Quan sát cách trừu tượng hóa dữ liệu họa sĩ và đặc biệt là biểu diễn họa sĩ dưới dạng các thủ tục giúp `beside` dễ triển khai như thế nào. Thủ tục `beside` không cần biết bất cứ điều gì về các chi tiết của các họa sĩ thành phần ngoài việc mỗi họa sĩ sẽ vẽ một cái gì đó trong khung được chỉ định của nó.

**Bài tập 2.50:** Hãy định nghĩa phép biến đổi `flip-horiz`, lật các họa sĩ theo chiều ngang và các phép biến đổi xoay các họa sĩ ngược chiều kim đồng hồ 180 độ và 270 độ.

**Bài tập 2.51:** Hãy định nghĩa phép toán `below` cho các họa sĩ. `Below` nhận hai họa sĩ làm đối số. Họa sĩ kết quả, khi nhận một khung, vẽ bằng họa sĩ đầu tiên ở dưới cùng của khung và với họa sĩ thứ hai ở trên cùng. Hãy định nghĩa `below` theo hai cách khác nhau—đầu tiên bằng cách viết một thủ tục tương tự như thủ tục `beside` đã cho ở trên và một lần nữa theo `beside` và các phép toán xoay thích hợp (từ [Bài tập 2.50](#Exercise-2_002e50)).

### Các Cấp Độ Ngôn Ngữ cho Thiết Kế Vững Chắc

Ngôn ngữ hình ảnh thực hành một số ý tưởng quan trọng mà chúng ta đã giới thiệu về trừu tượng hóa với các thủ tục và dữ liệu. Các trừu tượng hóa dữ liệu cơ bản, các họa sĩ, được triển khai bằng các biểu diễn thủ tục, cho phép ngôn ngữ xử lý các khả năng vẽ cơ bản khác nhau một cách thống nhất. Các phương tiện kết hợp thỏa mãn tính chất đóng, cho phép chúng ta dễ dàng xây dựng các thiết kế phức tạp. Cuối cùng, tất cả các công cụ để trừu tượng hóa các thủ tục đều có sẵn cho chúng ta để trừu tượng hóa các phương tiện kết hợp cho các họa sĩ.

Chúng ta cũng đã có được một cái nhìn thoáng qua về một ý tưởng quan trọng khác về các ngôn ngữ và thiết kế chương trình. Đây là cách tiếp cận *thiết kế phân tầng*, khái niệm rằng một hệ thống phức tạp nên được cấu trúc dưới dạng một chuỗi các cấp độ được mô tả bằng cách sử dụng một chuỗi các ngôn ngữ. Mỗi cấp độ được xây dựng bằng cách kết hợp các phần được coi là nguyên thủy ở cấp độ đó và các phần được xây dựng ở mỗi cấp độ được sử dụng làm các nguyên thủy ở cấp độ tiếp theo. Ngôn ngữ được sử dụng ở mỗi cấp độ của một thiết kế phân tầng có các nguyên thủy, phương tiện kết hợp và phương tiện