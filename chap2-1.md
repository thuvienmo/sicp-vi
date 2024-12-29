# 2.1 Giới thiệu về Trừu tượng hóa Dữ liệu

Trong [1.1.8](1_002e1.xhtml#g_t1_002e1_002e8), chúng ta đã lưu ý rằng một thủ tục được sử dụng như một phần tử trong việc tạo ra một thủ tục phức tạp hơn có thể được xem không chỉ là một tập hợp các thao tác cụ thể mà còn là một trừu tượng thủ tục. Điều đó có nghĩa là, các chi tiết về cách thủ tục được triển khai có thể được ẩn đi, và bản thân thủ tục cụ thể có thể được thay thế bằng bất kỳ thủ tục nào khác có cùng hành vi tổng thể. Nói cách khác, chúng ta có thể tạo ra một trừu tượng để tách biệt cách thủ tục sẽ được sử dụng khỏi các chi tiết về cách thủ tục sẽ được triển khai bằng các thủ tục nguyên thủy hơn. Khái niệm tương tự cho dữ liệu phức hợp được gọi là *trừu tượng hóa dữ liệu*. Trừu tượng hóa dữ liệu là một phương pháp cho phép chúng ta cô lập cách một đối tượng dữ liệu phức hợp được sử dụng khỏi các chi tiết về cách nó được xây dựng từ các đối tượng dữ liệu nguyên thủy hơn.

Ý tưởng cơ bản của trừu tượng hóa dữ liệu là cấu trúc các chương trình sẽ sử dụng các đối tượng dữ liệu phức hợp để chúng hoạt động trên "dữ liệu trừu tượng". Tức là, các chương trình của chúng ta nên sử dụng dữ liệu theo cách không đưa ra giả định nào về dữ liệu mà không thực sự cần thiết để thực hiện nhiệm vụ đang làm. Đồng thời, một biểu diễn dữ liệu "cụ thể" được xác định độc lập với các chương trình sử dụng dữ liệu. Giao diện giữa hai phần này của hệ thống của chúng ta sẽ là một tập hợp các thủ tục, được gọi là *bộ chọn* và *bộ xây dựng*, triển khai dữ liệu trừu tượng theo biểu diễn cụ thể. Để minh họa kỹ thuật này, chúng ta sẽ xem xét cách thiết kế một tập hợp các thủ tục để thao tác các số hữu tỉ.

## 2.1.1 Ví dụ: Các phép toán số học cho số hữu tỉ

Giả sử chúng ta muốn thực hiện các phép toán số học với số hữu tỉ. Chúng ta muốn có thể cộng, trừ, nhân và chia chúng, đồng thời kiểm tra xem hai số hữu tỉ có bằng nhau hay không.

Hãy bắt đầu bằng cách giả định rằng chúng ta đã có một cách để xây dựng một số hữu tỉ từ một tử số và một mẫu số. Chúng ta cũng giả định rằng, cho một số hữu tỉ, chúng ta có một cách để trích xuất (hoặc chọn) tử số và mẫu số của nó. Chúng ta hãy giả định thêm rằng bộ xây dựng và bộ chọn có sẵn dưới dạng các thủ tục:

- `(make-rat ⟨n⟩ ⟨d⟩)` trả về số hữu tỉ có tử số là số nguyên `⟨n⟩` và mẫu số là số nguyên `⟨d⟩`.
- `(numer ⟨x⟩)` trả về tử số của số hữu tỉ `⟨x⟩`.
- `(denom ⟨x⟩)` trả về mẫu số của số hữu tỉ `⟨x⟩`.

Ở đây, chúng ta đang sử dụng một chiến lược tổng hợp mạnh mẽ: *suy nghĩ theo mong muốn*. Chúng ta chưa nói cách một số hữu tỉ được biểu diễn hoặc cách các thủ tục `numer`, `denom` và `make-rat` nên được triển khai. Ngay cả như vậy, nếu chúng ta có ba thủ tục này, thì chúng ta có thể cộng, trừ, nhân, chia và kiểm tra tính bằng nhau bằng cách sử dụng các mối quan hệ sau:

$$\begin{array}{lll}
{\frac{n_{1}}{d_{1}} + \frac{n_{2}}{d_{2}}} & = & {\frac{n_{1}d_{2} + n_{2}d_{1}}{d_{1}d_{2}},} \\
{\frac{n_{1}}{d_{1}} - \frac{n_{2}}{d_{2}}} & = & {\frac{n_{1}d_{2} - n_{2}d_{1}}{d_{1}d_{2}},} \\
{\frac{n_{1}}{d_{1}} \times \frac{n_{2}}{d_{2}}} & = & {\frac{n_{1}n_{2}}{d_{1}d_{2}},} \\
\frac{n_{1}\,/\, d_{1}}{n_{2}\,/\, d_{2}} & = & {\frac{n_{1}d_{2}}{d_{1}n_{2}},} \\
\frac{n_{1}}{d_{1}} & = & {\frac{n_{2}}{d_{2}}\quad{\ if\ and\ only\ if\quad}n_{1}d_{2} = n_{2}d_{1}.} \\
\end{array}$$

Chúng ta có thể thể hiện các quy tắc này dưới dạng các thủ tục:

```scheme
(define (add-rat x y)
  (make-rat (+ (* (numer x) (denom y))
               (* (numer y) (denom x)))
            (* (denom x) (denom y))))

(define (sub-rat x y)
  (make-rat (- (* (numer x) (denom y))
               (* (numer y) (denom x)))
            (* (denom x) (denom y))))

(define (mul-rat x y)
  (make-rat (* (numer x) (numer y))
            (* (denom x) (denom y))))

(define (div-rat x y)
  (make-rat (* (numer x) (denom y))
            (* (denom x) (numer y))))

(define (equal-rat? x y)
  (= (* (numer x) (denom y))
     (* (numer y) (denom x))))
```

Bây giờ chúng ta đã có các phép toán trên số hữu tỉ được xác định theo các thủ tục bộ chọn và bộ xây dựng `numer`, `denom` và `make-rat`. Nhưng chúng ta vẫn chưa định nghĩa chúng. Những gì chúng ta cần là một số cách để ghép tử số và mẫu số lại với nhau để tạo thành một số hữu tỉ.

### Các cặp

Để cho phép chúng ta triển khai mức độ cụ thể của trừu tượng dữ liệu, ngôn ngữ của chúng ta cung cấp một cấu trúc phức hợp gọi là *cặp*, có thể được xây dựng bằng thủ tục nguyên thủy `cons`. Thủ tục này nhận hai đối số và trả về một đối tượng dữ liệu phức hợp chứa hai đối số làm các phần. Cho một cặp, chúng ta có thể trích xuất các phần bằng cách sử dụng các thủ tục nguyên thủy `car` và `cdr`.^[Tên `cons` là viết tắt của “construct” (xây dựng). Tên `car` và `cdr` bắt nguồn từ cách triển khai Lisp ban đầu trên IBM 704. Máy đó có một sơ đồ định địa chỉ cho phép tham chiếu đến các phần “địa chỉ” và “giảm dần” của một vị trí bộ nhớ. `Car` là viết tắt của "Contents of Address part of Register" (Nội dung của phần Địa chỉ của Thanh ghi) và `cdr` (phát âm là “could-er”) là viết tắt của “Contents of Decrement part of Register” (Nội dung của phần Giảm dần của Thanh ghi).] Do đó, chúng ta có thể sử dụng `cons`, `car` và `cdr` như sau:

```scheme
(define x (cons 1 2))

(car x)
1

(cdr x)
2
```

Lưu ý rằng một cặp là một đối tượng dữ liệu có thể được đặt tên và thao tác, giống như một đối tượng dữ liệu nguyên thủy. Hơn nữa, `cons` có thể được sử dụng để tạo thành các cặp mà các phần tử là các cặp, v.v.:

```scheme
(define x (cons 1 2))
(define y (cons 3 4))
(define z (cons x y))

(car (car z))
1

(car (cdr z))
3
```

Trong [2.2](2_002e2.xhtml#g_t2_002e2), chúng ta sẽ thấy khả năng kết hợp các cặp có nghĩa là các cặp có thể được sử dụng làm các khối xây dựng đa mục đích để tạo ra tất cả các loại cấu trúc dữ liệu phức tạp như thế nào. Nguyên thủy dữ liệu phức hợp đơn *cặp*, được triển khai bởi các thủ tục `cons`, `car` và `cdr`, là chất kết dính duy nhất mà chúng ta cần. Các đối tượng dữ liệu được xây dựng từ các cặp được gọi là dữ liệu *có cấu trúc danh sách*.

### Biểu diễn số hữu tỉ

Các cặp cung cấp một cách tự nhiên để hoàn thành hệ thống số hữu tỉ. Đơn giản chỉ cần biểu diễn một số hữu tỉ dưới dạng một cặp gồm hai số nguyên: một tử số và một mẫu số. Sau đó, `make-rat`, `numer` và `denom` được triển khai dễ dàng như sau:^[Một cách khác để định nghĩa bộ chọn và bộ xây dựng là]

```scheme
(define (make-rat n d) (cons n d))
(define (numer x) (car x))
(define (denom x) (cdr x))
```

Ngoài ra, để hiển thị kết quả của các tính toán của chúng ta, chúng ta có thể in các số hữu tỉ bằng cách in tử số, một dấu gạch chéo và mẫu số:^[`Display` là nguyên thủy Scheme để in dữ liệu. Nguyên thủy Scheme `newline` bắt đầu một dòng mới để in. Không thủ tục nào trong số này trả về một giá trị hữu ích, vì vậy trong các cách sử dụng `print-rat` bên dưới, chúng ta chỉ hiển thị những gì `print-rat` in, không phải những gì trình thông dịch in dưới dạng giá trị được trả về bởi `print-rat`.]

```scheme
(define (print-rat x)
  (newline)
  (display (numer x))
  (display "/")
  (display (denom x)))
```

Bây giờ chúng ta có thể thử các thủ tục số hữu tỉ của mình:

```scheme
(define one-half (make-rat 1 2))
(print-rat one-half)
1/2

(define one-third (make-rat 1 3))
(print-rat
 (add-rat one-half one-third))
5/6

(print-rat
 (mul-rat one-half one-third))
1/6

(print-rat
 (add-rat one-third one-third))
6/9
```

Như ví dụ cuối cùng cho thấy, việc triển khai số hữu tỉ của chúng ta không rút gọn các số hữu tỉ về dạng tối giản. Chúng ta có thể khắc phục điều này bằng cách thay đổi `make-rat`. Nếu chúng ta có một thủ tục `gcd` như trong [1.2.5](1_002e2.xhtml#g_t1_002e2_002e5) tạo ra ước số chung lớn nhất của hai số nguyên, chúng ta có thể sử dụng `gcd` để rút gọn tử số và mẫu số về dạng tối giản trước khi xây dựng cặp:

```scheme
(define (make-rat n d)
  (let ((g (gcd n d)))
    (cons (/ n g)
          (/ d g))))
```

Bây giờ chúng ta có

```scheme
(print-rat
 (add-rat one-third one-third))
2/3
```

như mong muốn. Sự sửa đổi này được thực hiện bằng cách thay đổi bộ xây dựng `make-rat` mà không thay đổi bất kỳ thủ tục nào (chẳng hạn như `add-rat` và `mul-rat`) triển khai các thao tác thực tế.

**Bài tập 2.1:** Hãy định nghĩa một phiên bản tốt hơn của `make-rat` xử lý cả các đối số dương và âm. `Make-rat` nên chuẩn hóa dấu sao cho nếu số hữu tỉ là dương, cả tử số và mẫu số đều dương, và nếu số hữu tỉ là âm, chỉ có tử số là âm.

## 2.1.2 Rào cản Trừu tượng

Trước khi tiếp tục với nhiều ví dụ hơn về dữ liệu phức hợp và trừu tượng hóa dữ liệu, chúng ta hãy xem xét một số vấn đề được nêu ra bởi ví dụ về số hữu tỉ. Chúng ta đã định nghĩa các phép toán số hữu tỉ theo bộ xây dựng `make-rat` và bộ chọn `numer` và `denom`. Nói chung, ý tưởng cơ bản của trừu tượng hóa dữ liệu là xác định cho mỗi loại đối tượng dữ liệu một tập hợp các phép toán cơ bản mà theo đó tất cả các thao tác của các đối tượng dữ liệu thuộc loại đó sẽ được thể hiện, và sau đó chỉ sử dụng các phép toán đó để thao tác dữ liệu.

Chúng ta có thể hình dung cấu trúc của hệ thống số hữu tỉ như được hiển thị trong [Hình 2.1](#Figure-2_002e1). Các đường ngang thể hiện *rào cản trừu tượng* cách ly các "mức độ" khác nhau của hệ thống. Ở mỗi cấp độ, rào cản ngăn cách các chương trình (phía trên) sử dụng trừu tượng dữ liệu với các chương trình (phía dưới) triển khai trừu tượng dữ liệu. Các chương trình sử dụng số hữu tỉ thao tác chúng chỉ theo các thủ tục được cung cấp "cho công chúng sử dụng" bởi gói số hữu tỉ: `add-rat`, `sub-rat`, `mul-rat`, `div-rat` và `equal-rat?`. Những thủ tục này, đến lượt chúng, được triển khai chỉ theo bộ xây dựng và bộ chọn `make-rat`, `numer` và `denom`, bản thân chúng được triển khai theo các cặp. Các chi tiết về cách các cặp được triển khai không liên quan đến phần còn lại của gói số hữu tỉ miễn là các cặp có thể được thao tác bằng cách sử dụng `cons`, `car` và `cdr`. Trên thực tế, các thủ tục ở mỗi cấp độ là các giao diện xác định các rào cản trừu tượng và kết nối các cấp độ khác nhau.

![](fig/chap2/Fig2.1d.std.svg 586.44x456.96)
**Hình 2.1:** Rào cản trừu tượng dữ liệu trong gói số hữu tỉ.

Ý tưởng đơn giản này có nhiều ưu điểm. Một ưu điểm là nó làm cho các chương trình dễ bảo trì và sửa đổi hơn nhiều. Bất kỳ cấu trúc dữ liệu phức tạp nào cũng có thể được biểu diễn theo nhiều cách khác nhau với các cấu trúc dữ liệu nguyên thủy do ngôn ngữ lập trình cung cấp. Tất nhiên, sự lựa chọn biểu diễn ảnh hưởng đến các chương trình hoạt động trên nó; do đó, nếu biểu diễn được thay đổi vào một thời điểm nào đó sau này, tất cả các chương trình như vậy có thể phải được sửa đổi cho phù hợp. Nhiệm vụ này có thể tốn thời gian và tốn kém trong trường hợp các chương trình lớn, trừ khi sự phụ thuộc vào biểu diễn được giới hạn bởi thiết kế trong một số ít mô-đun chương trình.

Ví dụ: một cách khác để giải quyết vấn đề rút gọn các số hữu tỉ về dạng tối giản là thực hiện việc rút gọn bất cứ khi nào chúng ta truy cập các phần của một số hữu tỉ, thay vì khi chúng ta xây dựng nó. Điều này dẫn đến các thủ tục bộ xây dựng và bộ chọn khác nhau:

```scheme
(define (make-rat n d)
  (cons n d))

(define (numer x)
  (let ((g (gcd (car x) (cdr x))))
    (/ (car x) g)))

(define (denom x)
  (let ((g (gcd (car x) (cdr x))))
    (/ (cdr x) g)))
```

Sự khác biệt giữa cách triển khai này và cách triển khai trước đó nằm ở thời điểm chúng ta tính toán `gcd`. Nếu trong việc sử dụng các số hữu tỉ thông thường của chúng ta, chúng ta truy cập các tử số và mẫu số của cùng một số hữu tỉ nhiều lần, thì tốt hơn là nên tính `gcd` khi các số hữu tỉ được xây dựng. Nếu không, chúng ta có thể tốt hơn nếu đợi đến thời điểm truy cập để tính `gcd`. Trong mọi trường hợp, khi chúng ta thay đổi từ biểu diễn này sang biểu diễn khác, các thủ tục `add-rat`, `sub-rat`, v.v. không phải sửa đổi chút nào.

Giới hạn sự phụ thuộc vào biểu diễn trong một số thủ tục giao diện giúp chúng ta thiết kế chương trình cũng như sửa đổi chúng, vì nó cho phép chúng ta duy trì sự linh hoạt để xem xét các cách triển khai khác. Để tiếp tục với ví dụ đơn giản của chúng ta, giả sử chúng ta đang thiết kế một gói số hữu tỉ và chúng ta không thể quyết định ban đầu có nên thực hiện `gcd` vào thời điểm xây dựng hay vào thời điểm chọn. Phương pháp trừu tượng hóa dữ liệu cho chúng ta một cách để trì hoãn quyết định đó mà không làm mất khả năng tiến bộ trên phần còn lại của hệ thống.

**Bài tập 2.2:** Xét vấn đề biểu diễn các đoạn thẳng trên một mặt phẳng. Mỗi đoạn được biểu diễn dưới dạng một cặp điểm: một điểm bắt đầu và một điểm kết thúc. Hãy định nghĩa bộ xây dựng `make-segment` và các bộ chọn `start-segment` và `end-segment` xác định biểu diễn của các đoạn theo các điểm. Hơn nữa, một điểm có thể được biểu diễn dưới dạng một cặp số: tọa độ x và tọa độ y. Theo đó, hãy chỉ định một bộ xây dựng `make-point` và các bộ chọn `x-point` và `y-point` xác định biểu diễn này. Cuối cùng, sử dụng các bộ chọn và bộ xây dựng của bạn, hãy định nghĩa một thủ tục `midpoint-segment` nhận một đoạn thẳng làm đối số và trả về trung điểm của nó (điểm có tọa độ là trung bình của tọa độ của các điểm cuối). Để thử các thủ tục của bạn, bạn sẽ cần một cách để in các điểm:

```scheme
(define (print-point p)
  (newline)
  (display "(")
  (display (x-point p))
  (display ",")
  (display (y-point p))
  (display ")"))
```

**Bài tập 2.3:** Hãy triển khai một biểu diễn cho các hình chữ nhật trên một mặt phẳng. (Gợi ý: Bạn có thể muốn sử dụng [Bài tập 2.2](#Exercise-2_002e2).) Theo các bộ xây dựng và bộ chọn của bạn, hãy tạo các thủ tục tính chu vi và diện tích của một hình chữ nhật đã cho. Bây giờ, hãy triển khai một biểu diễn khác cho các hình chữ nhật. Bạn có thể thiết kế hệ thống của mình với các rào cản trừu tượng phù hợp, sao cho các thủ tục chu vi và diện tích giống nhau sẽ hoạt động bằng cách sử dụng một trong hai biểu diễn không?

## 2.1.3 Dữ liệu có nghĩa là gì?

Chúng ta bắt đầu việc triển khai số hữu tỉ trong [2.1.1](#g_t2_002e1_002e1) bằng cách triển khai các phép toán số hữu tỉ `add-rat`, `sub-rat`, v.v. theo ba thủ tục không được chỉ định: `make-rat`, `numer` và `denom`. Tại thời điểm đó, chúng ta có thể nghĩ về các phép toán được xác định theo các đối tượng dữ liệu—tử số, mẫu số và số hữu tỉ—mà hành vi được chỉ định bởi ba thủ tục sau.

Nhưng chính xác thì *dữ liệu* có nghĩa là gì? Sẽ không đủ để nói "bất cứ điều gì được triển khai bởi các bộ chọn và bộ xây dựng đã cho." Rõ ràng, không phải mọi tập hợp tùy ý gồm ba thủ tục đều có thể đóng vai trò là cơ sở thích hợp cho việc triển khai số hữu tỉ. Chúng ta cần đảm bảo rằng, nếu chúng ta xây dựng một số hữu tỉ `x` từ một cặp số nguyên `n` và `d`, thì việc trích xuất `numer` và `denom` của `x` và chia chúng sẽ cho kết quả tương tự như việc chia `n` cho `d`. Nói cách khác, `make-rat`, `numer` và `denom` phải đáp ứng điều kiện là, đối với bất kỳ số nguyên `n` nào và bất kỳ số nguyên khác không `d` nào, nếu `x` là `(make-rat n d)`, thì

$$\frac{\text{(numer\ x)}}{\text{(denom\ x)}} = {\frac{\text{n}}{\text{d}}.}$$

Trên thực tế, đây là điều kiện duy nhất mà `make-rat`, `numer` và `denom` phải đáp ứng để tạo thành cơ sở phù hợp cho biểu diễn số hữu tỉ. Nói chung, chúng ta có thể coi dữ liệu được xác định bởi một số tập hợp các bộ chọn và bộ xây dựng, cùng với các điều kiện được chỉ định mà các thủ tục này phải đáp ứng để trở thành một biểu diễn hợp lệ.^[Đáng ngạc nhiên là ý tưởng này rất khó xây dựng một cách chặt chẽ. Có hai cách tiếp cận để đưa ra một công thức như vậy. Một, được tiên phong bởi C. A. R. [Hoare (1972)](References.xhtml#Hoare-_00281972_0029), được gọi là phương pháp *mô hình trừu tượng*. Nó chính thức hóa đặc tả "thủ tục cộng điều kiện" như được vạch ra trong ví dụ số hữu tỉ ở trên. Lưu ý rằng điều kiện đối với biểu diễn số hữu tỉ được nêu theo các sự kiện về số nguyên (tính bằng nhau và phép chia). Nói chung, các mô hình trừu tượng xác định các loại đối tượng dữ liệu mới theo các loại đối tượng dữ liệu đã được xác định trước đó. Các khẳng định về các đối tượng dữ liệu do đó có thể được kiểm tra bằng cách rút chúng thành các khẳng định về các đối tượng dữ liệu đã được xác định trước đó. Một cách tiếp cận khác, được giới thiệu bởi Zilles tại MIT, bởi Goguen, Thatcher, Wagner và Wright tại IBM (xem [Thatcher et al. 1978](References.xhtml#Thatcher-et-al_002e-1978)), và bởi Guttag tại Toronto (xem [Guttag 1977](References.xhtml#Guttag-1977)), được gọi là *đặc tả đại số*. Nó coi các "thủ tục" là các phần tử của một hệ thống đại số trừu tượng mà hành vi của nó được chỉ định bởi các tiên đề tương ứng với "điều kiện" của chúng ta và sử dụng các kỹ thuật của đại số trừu tượng để kiểm tra các khẳng định về các đối tượng dữ liệu. Cả hai phương pháp đều được khảo sát trong bài báo của [Liskov và Zilles (1975)](References.xhtml#Liskov-and-Zilles-_00281975_0029).]

Quan điểm này có thể được sử dụng để xác định không chỉ các đối tượng dữ liệu "cấp cao", chẳng hạn như số hữu tỉ, mà cả các đối tượng cấp thấp hơn. Hãy xem xét khái niệm về một cặp, mà chúng ta đã sử dụng để xác định các số hữu tỉ của mình. Chúng ta chưa bao giờ thực sự nói một cặp là gì, chỉ là ngôn ngữ cung cấp các thủ tục `cons`, `car` và `cdr` để hoạt động trên các cặp. Nhưng điều duy nhất chúng ta cần biết về ba thao tác này là nếu chúng ta ghép hai đối tượng lại với nhau bằng `cons`, chúng ta có thể truy xuất các đối tượng bằng `car` và `cdr`. Tức là, các phép toán thỏa mãn điều kiện là, đối với bất kỳ đối tượng `x` và `y` nào, nếu `z` là `(cons x y)` thì `(car z)` là `x` và `(cdr z)` là `y`. Thật vậy, chúng ta đã đề cập rằng ba thủ tục này được bao gồm như các nguyên thủy trong ngôn ngữ của chúng ta. Tuy nhiên, bất kỳ bộ ba thủ tục nào đáp ứng điều kiện trên đều có thể được sử dụng làm cơ sở để triển khai các cặp. Điểm này được minh họa rõ nét bởi thực tế là chúng ta có thể triển khai `cons`, `car` và `cdr` mà không sử dụng bất kỳ cấu trúc dữ liệu nào mà chỉ sử dụng các thủ tục. Đây là các định nghĩa:

```scheme
(define (cons x y)
  (define (dispatch m)
    (cond ((= m 0) x)
          ((= m 1) y)
          (else
           (error "Đối số không phải 0 hoặc 1:
                   CONS" m))))
  dispatch)

(define (car z) (z 0))
(define (cdr z) (z 1))
```

Việc sử dụng các thủ tục này tương ứng với không có gì giống như khái niệm trực quan của chúng ta về dữ liệu nên là gì. Tuy nhiên, tất cả những gì chúng ta cần làm để chứng minh rằng đây là một cách hợp lệ để biểu diễn các cặp là xác minh rằng các thủ tục này đáp ứng điều kiện đã nêu ở trên.

Điểm tinh tế cần lưu ý là giá trị được trả về bởi `(cons x y)` là một thủ tục—cụ thể là thủ tục `dispatch` được định nghĩa nội bộ, thủ tục này nhận một đối số và trả về `x` hoặc `y` tùy thuộc vào việc đối số là 0 hay 1. Tương ứng, `(car z)` được định nghĩa là áp dụng `z` cho 0. Do đó, nếu `z` là thủ tục được tạo bởi `(cons x y)`, thì `z` được áp dụng cho 0 sẽ cho kết quả `x`. Như vậy, chúng ta đã chỉ ra rằng `(car (cons x y))` cho kết quả `x`, như mong muốn. Tương tự, `(cdr (cons x y))` áp dụng thủ tục được trả về bởi `(cons x y)` cho 1, trả về `y`. Do đó, việc triển khai các cặp bằng thủ tục này là một cách triển khai hợp lệ và nếu chúng ta truy cập các cặp chỉ bằng cách sử dụng `cons`, `car` và `cdr`, chúng ta không thể phân biệt cách triển khai này với cách triển khai sử dụng cấu trúc dữ liệu "thực".

Mục đích của việc trưng bày biểu diễn thủ tục của các cặp không phải là ngôn ngữ của chúng ta hoạt động theo cách này (Scheme và các hệ thống Lisp nói chung triển khai các cặp trực tiếp, vì lý do hiệu quả) mà nó có thể hoạt động theo cách này. Biểu diễn thủ tục, mặc dù khó hiểu, là một cách hoàn toàn đầy đủ để biểu diễn các cặp, vì nó đáp ứng các điều kiện duy nhất mà các cặp cần đáp ứng. Ví dụ này cũng chứng minh rằng khả năng thao tác các thủ tục như các đối tượng sẽ tự động cung cấp khả năng biểu diễn dữ liệu phức hợp. Điều này có vẻ kỳ lạ bây giờ, nhưng các biểu diễn thủ tục của dữ liệu sẽ đóng một vai trò trung tâm trong danh mục lập trình của chúng ta. Phong cách lập trình này thường được gọi là *truyền thông điệp* và chúng ta sẽ sử dụng nó làm một công cụ cơ bản trong [Chương 3](Chapter-3.xhtml#Chapter-3) khi chúng ta giải quyết các vấn đề về mô hình hóa và mô phỏng.

**Bài tập 2.4:** Đây là một biểu diễn thủ tục thay thế của các cặp. Đối với biểu diễn này, hãy xác minh rằng `(car (cons x y))` cho kết quả `x` đối với bất kỳ đối tượng `x` và `y` nào.

```scheme
(define (cons x y)
  (lambda (m) (m x y)))

(define (car z)
  (z (lambda (p q) p)))
```

Định nghĩa tương ứng của `cdr` là gì? (Gợi ý: Để xác minh rằng điều này hoạt động, hãy sử dụng mô hình thay thế của [1.1.5](1_002e1.xhtml#g_t1_002e1_002e5).)

**Bài tập 2.5:** Hãy chỉ ra rằng chúng ta có thể biểu diễn các cặp số nguyên không âm chỉ bằng cách sử dụng các số và phép toán số học nếu chúng ta biểu diễn cặp $a$ và $b$ là số nguyên là tích $2^{a}3^{b}$. Hãy đưa ra các định nghĩa tương ứng của các thủ tục `cons`, `car` và `cdr`.

**Bài tập 2.6:** Trong trường hợp biểu diễn các cặp dưới dạng các thủ tục vẫn chưa đủ khó hiểu, hãy xem xét rằng, trong một ngôn ngữ có thể thao tác các thủ tục, chúng ta có thể làm mà không cần số (ít nhất là liên quan đến các số nguyên không âm) bằng cách triển khai 0 và phép cộng 1 như sau

```scheme
(define zero (lambda (f) (lambda (x) x)))

(define (add-1 n)
  (lambda (f) (lambda (x) (f ((n f) x)))))
```

Biểu diễn này được gọi là *số Church*, theo tên nhà phát minh ra nó, Alonzo Church, nhà logic học đã phát minh ra phép tính λ.

Hãy định nghĩa trực tiếp `one` và `two` (không theo `zero` và `add-1`). (Gợi ý: Sử dụng phép thay thế để đánh giá `(add-1 zero)`). Hãy đưa ra một định nghĩa trực tiếp của thủ tục cộng `+` (không theo ứng dụng lặp lại của `add-1`).

## 2.1.4 Bài tập mở rộng: Số học khoảng

Alyssa P. Hacker đang thiết kế một hệ thống để giúp mọi người giải quyết các vấn đề kỹ thuật. Một tính năng mà cô ấy muốn cung cấp trong hệ thống của mình là khả năng thao tác các đại lượng không chính xác (chẳng hạn như các thông số đo được của các thiết bị vật lý) với độ chính xác đã biết, để khi các phép tính được thực hiện với các đại lượng gần đúng như vậy, kết quả sẽ là các số có độ chính xác đã biết.

Các kỹ sư điện sẽ sử dụng hệ thống của Alyssa để tính toán các đại lượng điện. Đôi khi họ cần tính giá trị của một điện trở tương đương song song $R_{p}$ của hai điện trở $R_{1}$ và $R_{2}$ bằng công thức

$$R_{p}\, = \,{\frac{1}{1/R_{1} + 1/R_{2}}.}$$

Giá trị điện trở thường chỉ được biết đến với một dung sai nào đó được đảm bảo bởi nhà sản xuất điện trở. Ví dụ, nếu bạn mua một điện trở có nhãn "6,8 ôm với dung sai 10%", bạn chỉ có thể chắc chắn rằng điện trở có điện trở từ 6,8 - 0,68 = 6,12 và 6,8 + 0,68 = 7,48 ôm. Do đó, nếu bạn có một điện trở 6,8 ôm 10% song song với một điện trở 4,7 ôm 5%, điện trở của sự kết hợp có thể dao động từ khoảng 2,58 ôm (nếu hai điện trở ở các giới hạn dưới) đến khoảng 2,97 ôm (nếu hai điện trở ở các giới hạn trên).

Ý tưởng của Alyssa là triển khai "số học khoảng" như một tập hợp các phép toán số học để kết hợp các "khoảng" (các đối tượng đại diện cho phạm vi các giá trị có thể có của một đại lượng không chính xác). Kết quả của phép cộng, trừ, nhân hoặc chia hai khoảng cũng là một khoảng, đại diện cho phạm vi của kết quả.

Alyssa đưa ra giả thuyết về sự tồn tại của một đối tượng trừu tượng gọi là "khoảng" có hai điểm cuối: một giới hạn dưới và một giới hạn trên. Cô ấy cũng cho rằng, khi biết các điểm cuối của một khoảng, cô ấy có thể xây dựng khoảng bằng cách sử dụng bộ xây dựng dữ liệu `make-interval`. Alyssa đầu tiên viết một thủ tục để cộng hai khoảng. Cô lập luận rằng giá trị nhỏ nhất mà tổng có thể là tổng của hai giới hạn dưới và giá trị lớn nhất có thể là tổng của hai giới hạn trên:

```scheme
(define (add-interval x y)
  (make-interval (+ (lower-bound x)
                    (lower-bound y))
                 (+ (upper-bound x)
                    (upper-bound y))))
```

Alyssa cũng tính ra tích của hai khoảng bằng cách tìm giá trị nhỏ nhất và lớn nhất của tích của các giới hạn và sử dụng chúng làm giới hạn của khoảng kết quả. (`Min` và `max` là các nguyên thủy tìm giá trị nhỏ nhất hoặc lớn nhất của bất kỳ số lượng đối số nào.)

```scheme
(define (mul-interval x y)
  (let ((p1 (* (lower-bound x)
               (lower-bound y)))
        (p2 (* (lower-bound x)
               (upper-bound y)))
        (p3 (* (upper-bound x)
               (lower-bound y)))
        (p4 (* (upper-bound x)
               (upper-bound y))))
    (make-interval (min p1 p2 p3 p4)
                   (max p1 p2 p3 p4))))
```

Để chia hai khoảng, Alyssa nhân khoảng đầu tiên với nghịch đảo của khoảng thứ hai. Lưu ý rằng các giới hạn của khoảng nghịch đảo là nghịch đảo của giới hạn trên và nghịch đảo của giới hạn dưới, theo thứ tự đó.

```scheme
(define (div-interval x y)
  (mul-interval x
                (make-interval
                 (/ 1.0 (upper-bound y))
                 (/ 1.0 (lower-bound y)))))
```

**Bài tập 2.7:** Chương trình của Alyssa chưa hoàn chỉnh vì cô ấy chưa chỉ định cách triển khai trừu tượng khoảng. Đây là định nghĩa của bộ xây dựng khoảng:

```scheme
(define (make-interval a b) (cons a b))
```

Hãy định nghĩa bộ chọn `upper-bound` và `lower-bound` để hoàn thành việc triển khai.

**Bài tập 2.8:** Sử dụng lý luận tương tự như của Alyssa, hãy mô tả cách tính hiệu của hai khoảng. Hãy định nghĩa một thủ tục trừ tương ứng, được gọi là `sub-interval`.

**Bài tập 2.9:** *Độ rộng* của một khoảng là một nửa hiệu giữa giới hạn trên và giới hạn dưới của nó. Độ rộng là một thước đo độ không chắc chắn của số được chỉ định bởi khoảng. Đối với một số phép toán số học, độ rộng của kết quả khi kết hợp hai khoảng chỉ là một hàm của độ rộng của các khoảng đối số, trong khi đối với những phép toán khác, độ rộng của sự kết hợp không phải là một hàm của độ rộng của các khoảng đối số. Hãy chỉ ra rằng độ rộng của tổng (hoặc hiệu) của hai khoảng chỉ là một hàm của độ rộng của các khoảng đang được cộng (hoặc trừ). Hãy đưa ra các ví dụ để chỉ ra rằng điều này không đúng đối với phép nhân hoặc phép chia.

**Bài tập 2.10:** Ben Bitdiddle, một lập trình viên hệ thống chuyên gia, nhìn qua vai Alyssa và nhận xét rằng không rõ ý nghĩa của việc chia cho một khoảng trải dài qua số không. Hãy sửa đổi mã của Alyssa để kiểm tra điều kiện này và báo lỗi nếu nó xảy ra.

**Bài tập 2.11:** Tình cờ, Ben cũng nhận xét một cách khó hiểu: "Bằng cách kiểm tra dấu của các điểm cuối của các khoảng, có thể chia `mul-interval` thành chín trường hợp, trong đó chỉ có một trường hợp yêu cầu nhiều hơn hai phép nhân." Hãy viết lại thủ tục này bằng cách sử dụng đề xuất của Ben.

Sau khi gỡ lỗi chương trình của mình, Alyssa cho một người dùng tiềm năng xem, người này phàn nàn rằng chương trình của cô ấy giải quyết sai vấn đề. Anh ấy muốn một chương trình có thể xử lý các số được biểu diễn dưới dạng giá trị trung tâm và dung sai cộng; ví dụ, anh ấy muốn làm việc với các khoảng như 3,5 ± 0,15 chứ không phải [3,35, 3,65]. Alyssa quay lại bàn làm việc và khắc phục vấn đề này bằng cách cung cấp một bộ xây dựng thay thế và các bộ chọn thay thế:

```scheme
(define (make-center-width c w)
  (make-interval (- c w) (+ c w)))

(define (center i)