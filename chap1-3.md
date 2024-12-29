Chắc chắn rồi, đây là bản dịch sang tiếng Việt của các đoạn văn bản bạn đã cung cấp, tập trung vào các khái niệm toán học và khoa học máy tính:

# 1.3 Xây dựng các trừu tượng bằng các thủ tục bậc cao

Chúng ta đã thấy rằng các thủ tục, trên thực tế, là các trừu tượng mô tả các phép toán phức hợp trên các số, độc lập với các số cụ thể. Ví dụ, khi chúng ta viết

```scheme
(define (cube x) (* x x x))
```

chúng ta không nói về lũy thừa bậc ba của một số cụ thể, mà là về một phương pháp để lấy lũy thừa bậc ba của bất kỳ số nào. Tất nhiên, chúng ta có thể làm mà không cần định nghĩa thủ tục này, bằng cách luôn viết các biểu thức như

```scheme
(* 3 3 3)
(* x x x)
(* y y y)
```

và không bao giờ đề cập đến `cube` một cách rõ ràng. Điều này sẽ khiến chúng ta gặp bất lợi nghiêm trọng, buộc chúng ta luôn phải làm việc ở mức độ các phép toán cụ thể vốn là các nguyên thủy trong ngôn ngữ (phép nhân, trong trường hợp này) thay vì theo các phép toán cấp cao hơn. Các chương trình của chúng ta sẽ có thể tính lũy thừa bậc ba, nhưng ngôn ngữ của chúng ta sẽ thiếu khả năng diễn đạt khái niệm lũy thừa bậc ba. Một trong những điều chúng ta nên yêu cầu từ một ngôn ngữ lập trình mạnh mẽ là khả năng xây dựng các trừu tượng bằng cách gán tên cho các mẫu chung và sau đó làm việc trực tiếp với các trừu tượng. Các thủ tục cung cấp khả năng này. Đây là lý do tại sao tất cả các ngôn ngữ lập trình, ngoại trừ các ngôn ngữ nguyên thủy nhất, đều bao gồm các cơ chế để định nghĩa các thủ tục.

Tuy nhiên, ngay cả trong xử lý số, khả năng tạo ra các trừu tượng của chúng ta sẽ bị hạn chế nghiêm trọng nếu chúng ta bị giới hạn ở các thủ tục mà các tham số phải là số. Thông thường, cùng một mẫu lập trình sẽ được sử dụng với một số thủ tục khác nhau. Để thể hiện những mẫu như vậy thành các khái niệm, chúng ta sẽ cần xây dựng các thủ tục có thể chấp nhận các thủ tục làm đối số hoặc trả về các thủ tục làm giá trị. Các thủ tục thao tác các thủ tục được gọi là *thủ tục bậc cao*. Phần này cho thấy cách các thủ tục bậc cao có thể đóng vai trò là cơ chế trừu tượng mạnh mẽ, làm tăng đáng kể sức mạnh biểu đạt của ngôn ngữ của chúng ta.

## 1.3.1 Thủ tục như là các đối số

Xét ba thủ tục sau. Thủ tục đầu tiên tính tổng các số nguyên từ `a` đến `b`:

```scheme
(define (sum-integers a b)
  (if (> a b)
      0
      (+ a (sum-integers (+ a 1) b))))
```

Thủ tục thứ hai tính tổng các lũy thừa bậc ba của các số nguyên trong phạm vi đã cho:

```scheme
(define (sum-cubes a b)
  (if (> a b)
      0
      (+ (cube a)
         (sum-cubes (+ a 1) b))))
```

Thủ tục thứ ba tính tổng một dãy số hạng trong chuỗi

$$\frac{1}{1 \cdot 3} + \frac{1}{5 \cdot 7} + \frac{1}{9 \cdot 11} + {\ldots,}$$

hội tụ đến $\pi/8$ (rất chậm):^[Chuỗi này, thường được viết ở dạng tương đương $\frac{\pi}{4} = {1 - \frac{1}{3} + \frac{1}{5}} - {\frac{1}{7} + \ldots}$, là của Leibniz. Chúng ta sẽ xem cách sử dụng chuỗi này làm cơ sở cho một số thủ thuật số học thú vị trong [3.5.3](3_002e5.xhtml#g_t3_002e5_002e3).]

```scheme
(define (pi-sum a b)
  (if (> a b)
      0
      (+ (/ 1.0 (* a (+ a 2)))
         (pi-sum (+ a 4) b))))
```

Ba thủ tục này rõ ràng có chung một mẫu cơ bản. Chúng hầu hết giống hệt nhau, chỉ khác nhau về tên của thủ tục, hàm của `a` được sử dụng để tính toán số hạng được thêm vào và hàm cung cấp giá trị tiếp theo của `a`. Chúng ta có thể tạo ra từng thủ tục bằng cách điền vào các chỗ trống trong cùng một mẫu:

```scheme
(define (⟨name⟩ a b)
  (if (> a b)
      0
      (+ (⟨term⟩ a)
         (⟨name⟩ (⟨next⟩ a) b))))
```

Sự hiện diện của một mẫu chung như vậy là bằng chứng mạnh mẽ cho thấy có một trừu tượng hữu ích đang chờ được đưa ra bề mặt. Thật vậy, các nhà toán học từ lâu đã xác định trừu tượng của *tổng của một chuỗi* và phát minh ra "ký hiệu sigma", ví dụ

$${\sum\limits_{n = a}^{b}f(n)}\, = \,{f(a)} + \cdots + {f(b),}$$

để thể hiện khái niệm này. Sức mạnh của ký hiệu sigma là nó cho phép các nhà toán học xử lý khái niệm tổng hợp chứ không chỉ với các tổng cụ thể—ví dụ: để xây dựng các kết quả tổng quát về các tổng độc lập với chuỗi cụ thể đang được tổng.

Tương tự, với tư cách là nhà thiết kế chương trình, chúng ta muốn ngôn ngữ của mình đủ mạnh để có thể viết một thủ tục thể hiện khái niệm tổng hợp chứ không chỉ các thủ tục tính toán các tổng cụ thể. Chúng ta có thể làm điều đó dễ dàng trong ngôn ngữ thủ tục của mình bằng cách lấy mẫu chung được hiển thị ở trên và biến các "chỗ trống" thành các tham số hình thức:

```scheme
(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))
```

Lưu ý rằng `sum` lấy các đối số là các giới hạn dưới và trên `a` và `b` cùng với các thủ tục `term` và `next`. Chúng ta có thể sử dụng `sum` giống như bất kỳ thủ tục nào. Ví dụ: chúng ta có thể sử dụng nó (cùng với thủ tục `inc` tăng đối số của nó lên 1) để định nghĩa `sum-cubes`:

```scheme
(define (inc n) (+ n 1))

(define (sum-cubes a b)
  (sum cube a inc b))
```

Sử dụng điều này, chúng ta có thể tính tổng các lũy thừa bậc ba của các số nguyên từ 1 đến 10:

```scheme
(sum-cubes 1 10)
3025
```

Với sự trợ giúp của một thủ tục đồng nhất để tính toán số hạng, chúng ta có thể định nghĩa `sum-integers` theo `sum`:

```scheme
(define (identity x) x)

(define (sum-integers a b)
  (sum identity a inc b))
```

Sau đó, chúng ta có thể cộng các số nguyên từ 1 đến 10:

```scheme
(sum-integers 1 10)
55
```

Chúng ta cũng có thể định nghĩa `pi-sum` theo cách tương tự:^[Lưu ý rằng chúng ta đã sử dụng cấu trúc khối ([1.1.8](1_002e1.xhtml#g_t1_002e1_002e8)) để nhúng các định nghĩa của `pi-next` và `pi-term` bên trong `pi-sum`, vì các thủ tục này có khả năng không hữu ích cho bất kỳ mục đích nào khác. Chúng ta sẽ xem cách loại bỏ chúng hoàn toàn trong [1.3.2](#g_t1_002e3_002e2).]

```scheme
(define (pi-sum a b)
  (define (pi-term x)
    (/ 1.0 (* x (+ x 2))))
  (define (pi-next x)
    (+ x 4))
  (sum pi-term a pi-next b))
```

Sử dụng các thủ tục này, chúng ta có thể tính toán một giá trị gần đúng của $\pi$:

```scheme
(* 8 (pi-sum 1 1000))
3.139592655589783
```

Khi chúng ta có `sum`, chúng ta có thể sử dụng nó làm khối xây dựng để xây dựng các khái niệm tiếp theo. Ví dụ, tích phân xác định của một hàm $f$ giữa các giới hạn $a$ và $b$ có thể được tính gần đúng bằng số bằng công thức

$${\int_{a}^{b}\mspace{-5mu} f}\; = \;\left\lbrack \; f\left( a + \frac{dx}{2} \right) \right.\, + \,{f\left( a + dx + \frac{dx}{2} \right)}\, + \,{\left. f\left( a + 2dx + \frac{dx}{2} \right)\, + \,\ldots\; \right\rbrack dx}$$

cho các giá trị nhỏ của $dx$. Chúng ta có thể biểu thị điều này trực tiếp như một thủ tục:

```scheme
(define (integral f a b dx)
  (define (add-dx x) (+ x dx))
  (* (sum f (+ a (/ dx 2.0)) add-dx b)
     dx))

(integral cube 0 1 0.01)
.24998750000000042

(integral cube 0 1 0.001)
.249999875000001
```

(Giá trị chính xác của tích phân của `cube` giữa 0 và 1 là 1/4.)

**Bài tập 1.29:** Quy tắc Simpson là một phương pháp tích phân số chính xác hơn phương pháp được minh họa ở trên. Sử dụng Quy tắc Simpson, tích phân của một hàm $f$ giữa $a$ và $b$ được tính gần đúng bằng

$$\frac{h}{3}(y_{0} + {4y_{1}} + {2y_{2}} + {4y_{3}} + {2y_{4}} + \cdots + {2y_{n - 2}} + {4y_{n - 1} + y_{n}),$$

trong đó $h = (b - a)/n$, cho một số nguyên chẵn $n$, và $y_{k} = {f(a + kh)}$. (Tăng $n$ làm tăng độ chính xác của phép tính gần đúng.) Hãy định nghĩa một thủ tục nhận các đối số là $f$, $a$, $b$ và $n$ và trả về giá trị của tích phân, được tính bằng Quy tắc Simpson. Sử dụng thủ tục của bạn để tích phân `cube` giữa 0 và 1 (với $n = 100$ và $n = 1000$) và so sánh kết quả với các kết quả của thủ tục `integral` được hiển thị ở trên.

**Bài tập 1.30:** Thủ tục `sum` ở trên tạo ra một đệ quy tuyến tính. Thủ tục có thể được viết lại để tổng được thực hiện lặp đi lặp lại. Hãy chỉ ra cách thực hiện điều này bằng cách điền vào các biểu thức bị thiếu trong định nghĩa sau:

```scheme
(define (sum term a next b)
  (define (iter a result)
    (if ⟨??⟩
        ⟨??⟩
        (iter ⟨??⟩ ⟨??⟩)))
  (iter ⟨??⟩ ⟨??⟩))
```

**Bài tập 1.31:**

1. Thủ tục `sum` chỉ là đơn giản nhất trong vô số các trừu tượng tương tự có thể được nắm bắt dưới dạng các thủ tục bậc cao.^[Mục đích của [Bài tập 1.31](#Exercise-1_002e31) đến [Bài tập 1.33](#Exercise-1_002e33) là để chứng minh sức mạnh biểu đạt đạt được bằng cách sử dụng một trừu tượng thích hợp để hợp nhất nhiều phép toán dường như khác nhau. Tuy nhiên, mặc dù việc tích lũy và lọc là những ý tưởng thanh lịch, nhưng tay chúng ta hơi bị trói buộc khi sử dụng chúng tại thời điểm này vì chúng ta chưa có cấu trúc dữ liệu để cung cấp các phương tiện kết hợp phù hợp cho các trừu tượng này. Chúng ta sẽ quay lại các ý tưởng này trong [2.2.3](2_002e2.xhtml#g_t2_002e2_002e3) khi chúng ta trình bày cách sử dụng *dãy* làm giao diện để kết hợp các bộ lọc và bộ tích lũy để xây dựng các trừu tượng mạnh mẽ hơn. Chúng ta sẽ thấy ở đó những phương pháp này thực sự phát huy tác dụng như một cách tiếp cận mạnh mẽ và thanh lịch để thiết kế chương trình.] Viết một thủ tục tương tự có tên là `product` trả về tích các giá trị của một hàm tại các điểm trên một phạm vi đã cho. Hãy chỉ ra cách định nghĩa `factorial` theo `product`. Ngoài ra, hãy sử dụng `product` để tính toán các giá trị gần đúng của $\pi$ bằng công thức^[Công thức này được nhà toán học người Anh thế kỷ XVII John Wallis phát hiện ra.]

$$\frac{\pi}{4}\, = \,{\frac{2 \cdot 4 \cdot 4 \cdot 6 \cdot 6 \cdot 8 \cdot \cdots}{3 \cdot 3 \cdot 5 \cdot 5 \cdot 7 \cdot 7 \cdot \cdots}.}$$

2. Nếu thủ tục `product` của bạn tạo ra một quá trình đệ quy, hãy viết một thủ tục tạo ra một quá trình lặp. Nếu nó tạo ra một quá trình lặp, hãy viết một thủ tục tạo ra một quá trình đệ quy.

**Bài tập 1.32:**

1. Hãy chỉ ra rằng `sum` và `product` ([Bài tập 1.31](#Exercise-1_002e31)) đều là các trường hợp đặc biệt của một khái niệm tổng quát hơn gọi là `accumulate` kết hợp một tập hợp các số hạng, sử dụng một hàm tích lũy chung:

    ```scheme
    (accumulate
     combiner null-value term a next b)
    ```

    `Accumulate` lấy các đối số cùng thông số kỹ thuật số hạng và phạm vi như `sum` và `product`, cùng với một thủ tục `combiner` (của hai đối số) chỉ định cách số hạng hiện tại được kết hợp với sự tích lũy của các số hạng trước đó và một `null-value` chỉ định giá trị cơ bản nào để sử dụng khi các số hạng hết. Hãy viết `accumulate` và chỉ ra cách `sum` và `product` đều có thể được định nghĩa là các lệnh gọi đơn giản đến `accumulate`.
2. Nếu thủ tục `accumulate` của bạn tạo ra một quá trình đệ quy, hãy viết một thủ tục tạo ra một quá trình lặp. Nếu nó tạo ra một quá trình lặp, hãy viết một thủ tục tạo ra một quá trình đệ quy.

**Bài tập 1.33:** Bạn có thể có được một phiên bản tổng quát hơn nữa của `accumulate` ([Bài tập 1.32](#Exercise-1_002e32)) bằng cách giới thiệu khái niệm *bộ lọc* trên các số hạng sẽ được kết hợp. Đó là, chỉ kết hợp những số hạng bắt nguồn từ các giá trị trong phạm vi đáp ứng một điều kiện được chỉ định. Trừu tượng `filtered-accumulate` kết quả nhận các đối số giống như accumulate, cùng với một vị từ bổ sung của một đối số chỉ định bộ lọc. Hãy viết `filtered-accumulate` như một thủ tục. Hãy chỉ ra cách biểu thị những điều sau đây bằng cách sử dụng `filtered-accumulate`:

1. tổng các bình phương của các số nguyên tố trong khoảng $a$ đến $b$ (giả sử rằng bạn đã có một vị từ `prime?` được viết sẵn)
2. tích của tất cả các số nguyên dương nhỏ hơn $n$ mà nguyên tố cùng nhau với $n$ (tức là tất cả các số nguyên dương $i < n$ sao cho $\text{GCD}(i,n) = 1$).

## 1.3.2 Xây dựng thủ tục bằng `Lambda`

Khi sử dụng `sum` như trong [1.3.1](#g_t1_002e3_002e1), có vẻ như rất vụng về khi phải định nghĩa các thủ tục tầm thường như `pi-term` và `pi-next` chỉ để chúng ta có thể sử dụng chúng làm đối số cho thủ tục bậc cao của mình. Thay vì định nghĩa `pi-next` và `pi-term`, sẽ thuận tiện hơn nếu có cách trực tiếp chỉ định "thủ tục trả về đầu vào của nó được tăng thêm 4" và "thủ tục trả về nghịch đảo của đầu vào của nó nhân với đầu vào của nó cộng với 2". Chúng ta có thể làm điều này bằng cách giới thiệu dạng đặc biệt `lambda`, tạo ra các thủ tục. Sử dụng `lambda`, chúng ta có thể mô tả những gì chúng ta muốn như

```scheme
(lambda (x) (+ x 4))
```

và

```scheme
(lambda (x) (/ 1.0 (* x (+ x 2))))
```

Sau đó, thủ tục `pi-sum` của chúng ta có thể được biểu thị mà không cần định nghĩa bất kỳ thủ tục phụ trợ nào như

```scheme
(define (pi-sum a b)
  (sum (lambda (x) (/ 1.0 (* x (+ x 2))))
       a
       (lambda (x) (+ x 4))
       b))
```

Một lần nữa sử dụng `lambda`, chúng ta có thể viết thủ tục `integral` mà không cần phải định nghĩa thủ tục phụ trợ `add-dx`:

```scheme
(define (integral f a b dx)
  (* (sum f (+ a (/ dx 2.0))
            (lambda (x) (+ x dx))
            b)
     dx))
```

Nói chung, `lambda` được sử dụng để tạo các thủ tục theo cùng một cách như `define`, ngoại trừ việc không có tên nào được chỉ định cho thủ tục:

```scheme
(lambda (⟨formal-parameters⟩) ⟨body⟩)
```

Thủ tục kết quả cũng là một thủ tục như một thủ tục được tạo bằng `define`. Sự khác biệt duy nhất là nó không được liên kết với bất kỳ tên nào trong môi trường. Trong thực tế,

```scheme
(define (plus4 x) (+ x 4))
```

tương đương với

```scheme
(define plus4 (lambda (x) (+ x 4)))
```

Chúng ta có thể đọc một biểu thức `lambda` như sau:

```example
(lambda                     (x)     (+   x     4))
    |                        |       |   |     |
thủ tục của một đối số x cộng x và 4
```

Giống như bất kỳ biểu thức nào có một thủ tục làm giá trị của nó, một biểu thức `lambda` có thể được sử dụng làm toán tử trong một tổ hợp như

```scheme
((lambda (x y z) (+ x y (square z))) 1 2 3)
12
```

hoặc, tổng quát hơn, trong bất kỳ ngữ cảnh nào mà chúng ta thường sử dụng tên thủ tục.^[Sẽ rõ ràng hơn và ít gây khó khăn hơn cho những người học Lisp nếu một tên rõ ràng hơn `lambda`, chẳng hạn như `make-procedure`, được sử dụng. Nhưng quy ước đã được củng cố vững chắc. Ký hiệu được chấp nhận từ phép tính λ, một hình thức toán học được nhà lôgic toán học Alonzo [Church (1941)](References.xhtml#Church-_00281941_0029) giới thiệu. Church đã phát triển phép tính λ để cung cấp một nền tảng chặt chẽ để nghiên cứu các khái niệm về hàm và ứng dụng hàm. Phép tính λ đã trở thành một công cụ cơ bản cho các nghiên cứu toán học về ngữ nghĩa của các ngôn ngữ lập trình.]

### Sử dụng `let` để tạo các biến cục bộ

Một cách sử dụng khác của `lambda` là tạo các biến cục bộ. Chúng ta thường cần các biến cục bộ trong các thủ tục của mình khác với những biến đã được liên kết dưới dạng các tham số hình thức. Ví dụ, giả sử chúng ta muốn tính toán hàm

$${f(x,y)}\, = \,{x(1 + xy)^{2}} + {y(1 - y)} + {(1 + xy)(1 - y),}$$

mà chúng ta cũng có thể biểu thị là

$$\begin{array}{lll}
a & = & {1 + xy,} \\
{\phantom{(x,y)}b} & = & {1 - y,} \\
{f(x,y)} & = & {{xa^{2}} + {yb} + {ab.}} \\
\end{array}$$

Khi viết một thủ tục để tính toán $f$, chúng ta muốn bao gồm các biến cục bộ không chỉ $x$ và $y$ mà còn cả tên của các đại lượng trung gian như $a$ và $b$. Một cách để thực hiện điều này là sử dụng một thủ tục phụ trợ để liên kết các biến cục bộ:

```scheme
(define (f x y)
  (define (f-helper a b)
    (+ (* x (square a))
       (* y b)
       (* a b)))
  (f-helper (+ 1 (* x y))
            (- 1 y)))
```

Tất nhiên, chúng ta có thể sử dụng biểu thức `lambda` để chỉ định một thủ tục ẩn danh để liên kết các biến cục bộ của chúng ta. Phần thân của `f` sau đó trở thành một lệnh gọi duy nhất đến thủ tục đó:

```scheme
(define (f x y)
  ((lambda (a b)
     (+ (* x (square a))
        (* y b)
        (* a b)))
   (+ 1 (* x y))
   (- 1 y)))
```

Cấu trúc này rất hữu ích nên có một dạng đặc biệt gọi là `let` để sử dụng nó thuận tiện hơn. Sử dụng `let`, thủ tục `f` có thể được viết là

```scheme
(define (f x y)
  (let ((a (+ 1 (* x y)))
        (b (- 1 y)))
    (+ (* x (square a))
       (* y b)
       (* a b))))
```

Dạng chung của biểu thức `let` là

```scheme
(let ((⟨var₁⟩ ⟨exp₁⟩)
      (⟨var₂⟩ ⟨exp₂⟩)
      …
      (⟨varₙ⟩ ⟨expₙ⟩))
  ⟨body⟩)
```

có thể được coi là nói

```example
cho ⟨var₁⟩ có giá trị ⟨exp₁⟩ và
    ⟨var₂⟩ có giá trị ⟨exp₂⟩ và
    …
    ⟨varₙ⟩ có giá trị ⟨expₙ⟩
  trong ⟨body⟩
```

Phần đầu tiên của biểu thức `let` là một danh sách các cặp tên-biểu thức. Khi `let` được đánh giá, mỗi tên được liên kết với giá trị của biểu thức tương ứng. Phần thân của `let` được đánh giá với các tên này được liên kết dưới dạng các biến cục bộ. Cách điều này xảy ra là biểu thức `let` được diễn giải như một cú pháp thay thế cho

```scheme
((lambda (⟨var₁⟩ … ⟨varₙ⟩)
   ⟨body⟩)
 ⟨exp₁⟩
 …
 ⟨expₙ⟩)
```

Không có cơ chế mới nào được yêu cầu trong trình thông dịch để cung cấp các biến cục bộ. Một biểu thức `let` chỉ đơn giản là đường cú pháp cho ứng dụng `lambda` cơ bản.

Chúng ta có thể thấy từ sự tương đương này rằng phạm vi của một biến được chỉ định bởi một biểu thức `let` là phần thân của `let`. Điều này ngụ ý rằng:

- `Let` cho phép liên kết các biến cục bộ nhất có thể với nơi chúng được sử dụng. Ví dụ: nếu giá trị của `x` là 5, thì giá trị của biểu thức

    ```scheme
    (+ (let ((x 3))
         (+ x (* x 10)))
       x)
    ```

    là 38. Ở đây, `x` trong phần thân của `let` là 3, vì vậy giá trị của biểu thức `let` là 33. Mặt khác, `x` là đối số thứ hai của `+` ngoài cùng vẫn là 5.

- Giá trị của các biến được tính toán bên ngoài `let`. Điều này quan trọng khi các biểu thức cung cấp giá trị cho các biến cục bộ phụ thuộc vào các biến có cùng tên với chính các biến cục bộ. Ví dụ: nếu giá trị của `x` là 2, thì biểu thức

    ```scheme
    (let ((x 3)
          (y (+ x 2)))
      (* x y))
    ```

    sẽ có giá trị là 12 vì, bên trong phần thân của `let`, `x` sẽ là 3 và `y` sẽ là 4 (tức là `x` bên ngoài cộng với 2).

Đôi khi chúng ta có thể sử dụng các định nghĩa nội bộ để có được hiệu ứng tương tự như với `let`. Ví dụ: chúng ta có thể định nghĩa thủ tục `f` ở trên là

```scheme
(define (f x y)
  (define a
    (+ 1 (* x y)))
  (define b (- 1 y))
  (+ (* x (square a))
     (* y b)
     (* a b)))
```

Tuy nhiên, chúng ta thích sử dụng `let` trong các tình huống như thế này và chỉ sử dụng `define` bên trong cho các thủ tục nội bộ.^[Việc hiểu các định nghĩa nội bộ đủ rõ để đảm bảo rằng một chương trình có nghĩa là những gì chúng ta dự định có nghĩa đòi hỏi một mô hình chi tiết hơn về quy trình đánh giá so với những gì chúng ta đã trình bày trong chương này. Tuy nhiên, những điều tinh tế không phát sinh với các định nghĩa bên trong của thủ tục. Chúng ta sẽ quay lại vấn đề này trong [4.1.6](4_002e1.xhtml#g_t4_002e1_002e6) sau khi chúng ta tìm hiểu thêm về đánh giá.]

**Bài tập 1.34:** Giả sử chúng ta định nghĩa thủ tục

```scheme
(define (f g) (g 2))
```

Sau đó chúng ta có

```scheme
(f square)
4

(f (lambda (z) (* z (+ z 1))))
6
```

Điều gì xảy ra nếu chúng ta (một cách nghịch ngợm) yêu cầu trình thông dịch đánh giá sự kết hợp `(f f)`? Hãy giải thích.

## 1.3.3 Thủ tục như là các phương pháp chung

Chúng ta đã giới thiệu các thủ tục phức hợp trong [1.1.4](1_002e1.xhtml#g_t1_002e1_002e4) như một cơ chế để trừu tượng hóa các mẫu của các phép toán số để làm cho chúng độc lập với các số cụ thể liên quan. Với các thủ tục bậc cao, chẳng hạn như thủ tục `integral` trong [1.3.1](#g_t1_002e3_002e1), chúng ta bắt đầu thấy một loại trừu tượng mạnh mẽ hơn: các thủ tục được sử dụng để thể hiện các phương pháp tính toán chung, độc lập với các hàm cụ thể liên quan. Trong phần này, chúng ta thảo luận về hai ví dụ chi tiết hơn—các phương pháp chung để tìm số không và điểm cố định của các hàm—và chỉ ra cách các phương pháp này có thể được thể hiện trực tiếp dưới dạng các thủ tục.

### Tìm nghiệm của phương trình bằng phương pháp chia đôi khoảng

*Phương pháp chia đôi khoảng* là một kỹ thuật đơn giản nhưng mạnh mẽ để tìm nghiệm của phương trình $f(x) = 0$, trong đó $f$ là một hàm liên tục. Ý tưởng là, nếu chúng ta có các điểm $a$ và $b$ sao cho $f(a) < 0 < f(b)$, thì $f$ phải có ít nhất một số không giữa $a$ và $b$. Để xác định vị trí một số không, hãy đặt $x$ là trung bình của $a$ và $b$, và tính toán $f(x)$. Nếu $f(x) > 0$, thì $f$ phải có một số không giữa $a$ và $x$. Nếu $f(x) < 0$, thì $f$ phải có một số không giữa $x$ và $b$. Tiếp tục theo cách này, chúng ta có thể xác định các khoảng nhỏ hơn và nhỏ hơn mà $f$ phải có một số không. Khi chúng ta đạt đến một điểm mà khoảng đủ nhỏ, quá trình sẽ dừng lại. Vì khoảng không chắc chắn giảm đi một nửa ở mỗi bước của quá trình, số bước cần thiết tăng theo $\Theta(\log(L\,/\, T))$, trong đó $L$ là độ dài của khoảng ban đầu và $T$ là dung sai lỗi (nghĩa là, kích thước của khoảng mà chúng ta sẽ coi là "đủ nhỏ"). Đây là một thủ tục thực hiện chiến lược này:

```scheme
(define (search f neg-point pos-point)
  (let ((midpoint
         (average neg-point pos-point)))
    (if (close-enough? neg-point pos-point)
        midpoint
        (let ((test-value (f midpoint)))
          (cond
           ((positive? test-value)
            (search f neg-point midpoint))
           ((negative? test-value)
            (search f midpoint pos-point))
           (else midpoint))))))
```

Chúng ta giả định rằng ban đầu chúng ta có hàm $f$ cùng với các điểm mà các giá trị của nó là âm và dương. Đầu tiên, chúng ta tính điểm giữa của hai điểm đã cho. Tiếp theo, chúng ta kiểm tra xem khoảng đã cho có đủ nhỏ hay không, và nếu có, chúng ta chỉ cần trả về điểm giữa làm câu trả lời của mình. Nếu không, chúng ta tính giá trị của $f$ tại điểm giữa làm giá trị thử nghiệm. Nếu giá trị thử nghiệm là dương, thì chúng ta tiếp tục quá trình với một khoảng mới chạy từ điểm âm ban đầu đến điểm giữa. Nếu giá trị thử nghiệm là âm, chúng ta tiếp tục với khoảng từ điểm giữa đến điểm dương. Cuối cùng, có khả năng giá trị thử nghiệm là 0, trong trường hợp đó điểm giữa chính là nghiệm mà chúng ta đang tìm kiếm.

Để kiểm tra xem các điểm cuối có "đủ gần" hay không, chúng ta có thể sử dụng một thủ tục tương tự như thủ tục được sử dụng trong [1.1.7](1_002e1.xhtml#g_t1_002e1_002e7) để tính căn bậc hai:^[Chúng ta đã sử dụng 0,001 làm một số "nhỏ" đại diện để chỉ dung sai cho lỗi chấp nhận được trong phép tính. Dung sai thích hợp cho một phép tính thực tế phụ thuộc vào vấn đề cần giải quyết và các giới hạn của máy tính và thuật toán. Đây thường là một cân nhắc rất tinh tế, đòi hỏi sự trợ giúp của một nhà phân tích số hoặc một số loại nhà ảo thuật khác.]

```scheme
(define (close-enough? x y)
  (< (abs (- x y)) 0.001))
```

`Search` rất khó sử dụng trực tiếp, vì chúng ta có thể vô tình đưa cho nó các điểm mà giá trị của $f$ không có dấu yêu cầu, trong trường hợp đó chúng ta sẽ nhận được câu trả lời sai. Thay vào đó, chúng ta sẽ sử dụng `search` thông qua thủ tục sau, thủ tục này kiểm tra xem điểm cuối nào có giá trị hàm âm và điểm nào có giá trị dương, đồng thời gọi thủ tục `search` cho phù hợp. Nếu hàm có cùng dấu trên hai điểm đã cho, thì không thể sử dụng phương pháp chia đôi khoảng, trong trường hợp đó, thủ tục sẽ báo lỗi.^[Điều này có thể được thực hiện bằng cách sử dụng `error`, nhận các đối số là một số mục được in dưới dạng thông báo lỗi.]

```scheme
(define (half-interval-method f a b)
  (let ((a-value (f a))
        (b-value (f b)))
    (cond ((and (negative? a-value)
                (positive? b-value))
           (search f a b))
          ((and (negative? b-value)
                (positive? a-value))
           (search f b a))
          (else
           (error "Các giá trị không có
                   dấu đối nhau" a b)))))
```

Ví dụ sau sử dụng phương pháp chia đôi khoảng để tính gần đúng $\pi$ là nghiệm giữa 2 và 4 của $\sin x = 0$:

```scheme
(half-interval-method sin 2.0 4.0)
3.14111328125
```

Đây là một ví dụ khác, sử dụng phương pháp chia đôi khoảng để tìm kiếm nghiệm của phương trình $x^{3} - 2x - 3 = 0$ giữa 1 và 2:

```scheme
(half-interval-method
 (lambda (x) (- (* x x x) (* 2 x) 3))
 1.0
 2.0)
1.89306640625
```

### Tìm điểm cố định của các hàm

Một số $x$ được gọi là *điểm cố định* của một hàm $f$ nếu $x$ thỏa mãn phương trình $f(x) = x$. Đối với một số hàm $f$, chúng ta có thể xác định vị trí một điểm cố định bằng cách bắt đầu với một phỏng đoán ban đầu và áp dụng $f$ lặp đi lặp lại,

$${f(x),}\quad{f(f(x)),}\quad{f(f(f(x))),}\quad{\ldots,}$$

cho đến khi giá trị không thay đổi nhiều. Sử dụng ý tưởng này, chúng ta có thể đưa ra một thủ tục `fixed-point` lấy các đầu vào là một hàm và một phỏng đoán ban đầu và tạo ra một phép tính gần đúng cho một điểm cố định của hàm. Chúng ta áp dụng hàm lặp đi lặp lại cho đến khi tìm thấy hai giá trị liên tiếp có sự khác biệt nhỏ hơn một dung sai được quy định:

```scheme
(define tolerance 0.00001)

(define (fixed-point f first-guess)
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2))
       tolerance))
  (define (try guess)
    (let ((next (f guess)))
      (if (close-enough? guess next)
          next
          (try next))))
  (try first-guess))
```

Ví dụ, chúng ta có thể sử dụng phương pháp này để tính gần đúng điểm cố định của hàm cosin, bắt đầu với 1 làm phép tính gần đúng ban đầu:^[Hãy thử điều này trong một bài giảng nhàm chán: Đặt máy tính của bạn ở chế độ radian và sau đó liên tục nhấn nút `cos` cho đến khi bạn nhận được điểm cố định.]

```scheme
(fixed-point cos 1.0)
.7390822985224023
```

Tương tự, chúng ta có thể tìm một nghiệm cho phương trình $y = \sin y + \cos y$:

```scheme
(fixed-point (lambda (y) (+ (sin y) (cos y)))
             1.0)
1.2587315