## 1.2 Các Thủ Tục và Các Tiến Trình Chúng Tạo Ra

Chúng ta đã xem xét các yếu tố của lập trình: Chúng ta đã sử dụng các phép toán số học cơ bản, chúng ta đã kết hợp các phép toán này và chúng ta đã trừu tượng hóa các phép toán phức tạp này bằng cách định nghĩa chúng là các thủ tục hợp thành. Nhưng điều đó vẫn chưa đủ để cho phép chúng ta nói rằng chúng ta biết cách lập trình. Tình huống của chúng ta tương tự như một người đã học các quy tắc về cách các quân cờ di chuyển trong cờ vua nhưng không biết gì về các khai cuộc, chiến thuật hoặc chiến lược điển hình. Giống như người chơi cờ vua mới vào nghề, chúng ta vẫn chưa biết các mô hình sử dụng phổ biến trong lĩnh vực này. Chúng ta thiếu kiến ​​thức về những nước đi nào đáng thực hiện (những thủ tục nào đáng định nghĩa). Chúng ta thiếu kinh nghiệm để dự đoán hậu quả của việc thực hiện một nước đi (thực thi một thủ tục).

Khả năng hình dung ra hậu quả của các hành động đang được xem xét là rất quan trọng để trở thành một lập trình viên chuyên nghiệp, giống như trong bất kỳ hoạt động sáng tạo tổng hợp nào. Ví dụ, để trở thành một nhiếp ảnh gia chuyên nghiệp, người ta phải học cách nhìn một cảnh và biết mỗi vùng sẽ xuất hiện tối như thế nào trên bản in cho mỗi lựa chọn có thể về độ phơi sáng và điều kiện phát triển. Chỉ sau đó, người ta mới có thể suy luận ngược lại, lập kế hoạch khung, ánh sáng, độ phơi sáng và phát triển để có được các hiệu ứng mong muốn. Điều đó cũng đúng với lập trình, nơi chúng ta đang lập kế hoạch cho quá trình hành động mà một tiến trình sẽ thực hiện và nơi chúng ta kiểm soát tiến trình bằng một chương trình. Để trở thành chuyên gia, chúng ta phải học cách hình dung các tiến trình được tạo ra bởi các loại thủ tục khác nhau. Chỉ sau khi chúng ta đã phát triển được một kỹ năng như vậy, chúng ta mới có thể học cách xây dựng một cách đáng tin cậy các chương trình thể hiện hành vi mong muốn.

Một thủ tục là một mô hình cho sự *tiến hóa cục bộ* của một tiến trình tính toán. Nó chỉ định cách mỗi giai đoạn của tiến trình được xây dựng dựa trên giai đoạn trước đó. Chúng ta muốn có thể đưa ra các phát biểu về hành vi tổng thể, hay *toàn cục*, của một tiến trình mà sự tiến hóa cục bộ của nó đã được chỉ định bởi một thủ tục. Điều này rất khó thực hiện nói chung, nhưng ít nhất chúng ta có thể cố gắng mô tả một số mô hình tiến hóa tiến trình điển hình.

Trong phần này, chúng ta sẽ xem xét một số "hình dạng" phổ biến cho các tiến trình được tạo ra bởi các thủ tục đơn giản. Chúng ta cũng sẽ điều tra tốc độ mà các tiến trình này tiêu thụ các tài nguyên tính toán quan trọng về thời gian và không gian. Các thủ tục mà chúng ta sẽ xem xét rất đơn giản. Vai trò của chúng giống như vai trò của các mẫu thử trong nhiếp ảnh: như các mẫu nguyên mẫu được đơn giản hóa quá mức, chứ không phải là các ví dụ thực tế trong chính chúng.

## 1.2.1 Đệ Quy Tuyến Tính và Lặp

Chúng ta bắt đầu bằng cách xem xét hàm giai thừa, được định nghĩa bởi

$$n!\, = \,{n \cdot (n - 1)} \cdot {(n - 2)}\cdots{3 \cdot 2 \cdot 1.}$$

Có nhiều cách để tính giai thừa. Một cách là sử dụng quan sát rằng $n!$ bằng $n$ lần $(n - 1)!$ đối với bất kỳ số nguyên dương $n$ nào:

$$n!\, = \,{n \cdot \lbrack(n - 1)} \cdot {(n - 2)}\cdots{3 \cdot 2 \cdot 1\rbrack}\, = \,{n \cdot (n - 1)!}.$$

Vì vậy, chúng ta có thể tính $n!$ bằng cách tính $(n - 1)!$ và nhân kết quả với $n$. Nếu chúng ta thêm quy định rằng 1! bằng 1, quan sát này sẽ chuyển trực tiếp thành một thủ tục:

``` {.scheme}
(define (factorial n)
  (if (= n 1) 
      1 
      (* n (factorial (- n 1)))))
```

Chúng ta có thể sử dụng mô hình thay thế của [1.1.5](1_002e1.xhtml#g_t1_002e1_002e5) để theo dõi thủ tục này trong hành động tính 6!, như được hiển thị trong [Hình 1.3](#Hình-1_002e3).

![](fig/chap1/Fig1.3d.std.svg 630.96x377.16)
**Hình 1.3:** Một tiến trình đệ quy tuyến tính để tính 6!.

Bây giờ hãy xem xét một góc độ khác về việc tính giai thừa. Chúng ta có thể mô tả một quy tắc để tính $n!$ bằng cách chỉ định rằng trước tiên chúng ta nhân 1 với 2, sau đó nhân kết quả với 3, sau đó với 4, v.v. cho đến khi chúng ta đạt đến $n$. Cụ thể hơn, chúng ta duy trì một tích đang chạy, cùng với một bộ đếm đếm từ 1 đến $n$. Chúng ta có thể mô tả phép tính bằng cách nói rằng bộ đếm và tích đồng thời thay đổi từ bước này sang bước tiếp theo theo quy tắc

``` {.example}
product 
  ←
 counter * product
counter 
  ←
 counter + 1
```

và quy định rằng $n!$ là giá trị của tích khi bộ đếm vượt quá $n$.

Một lần nữa, chúng ta có thể diễn giải lại mô tả của mình thành một thủ tục để tính giai thừa:^[Trong một chương trình thực tế, có lẽ chúng ta sẽ sử dụng cấu trúc khối được giới thiệu trong phần trước để ẩn định nghĩa của `fact-iter`:]

``` {.scheme}
(define (factorial n) 
  (fact-iter 1 1 n))

(define (fact-iter product counter max-count)
  (if (> counter max-count)
      product
      (fact-iter (* counter product)
                 (+ counter 1)
                 max-count)))
```

Như trước đây, chúng ta có thể sử dụng mô hình thay thế để hình dung quá trình tính 6!, như được hiển thị trong [Hình 1.4](#Hình-1_002e4).

![](fig/chap1/Fig1.4d.std.svg 280.8x279.72)
**Hình 1.4:** Một tiến trình lặp tuyến tính để tính 6!.

So sánh hai tiến trình. Từ một quan điểm, chúng dường như không khác nhau chút nào. Cả hai đều tính cùng một hàm toán học trên cùng một miền và mỗi hàm đều yêu cầu một số bước tỷ lệ với $n$ để tính $n!$. Thật vậy, cả hai tiến trình thậm chí còn thực hiện cùng một chuỗi các phép nhân, thu được cùng một chuỗi các tích riêng phần. Mặt khác, khi chúng ta xem xét "hình dạng" của hai tiến trình, chúng ta thấy rằng chúng tiến hóa khá khác nhau.

Xem xét tiến trình đầu tiên. Mô hình thay thế cho thấy một hình dạng mở rộng theo sau là sự co lại, được biểu thị bằng mũi tên trong [Hình 1.3](#Hình-1_002e3). Sự mở rộng xảy ra khi tiến trình xây dựng một chuỗi các *thao tác bị trì hoãn* (trong trường hợp này, một chuỗi các phép nhân). Sự co lại xảy ra khi các thao tác thực sự được thực hiện. Loại tiến trình này, được đặc trưng bởi một chuỗi các thao tác bị trì hoãn, được gọi là *tiến trình đệ quy*. Để thực hiện tiến trình này, trình thông dịch cần theo dõi các thao tác sẽ được thực hiện sau này. Trong tính toán $n!$, độ dài của chuỗi các phép nhân bị trì hoãn và do đó lượng thông tin cần thiết để theo dõi nó, tăng tuyến tính với $n$ (tỷ lệ với $n$), giống như số lượng các bước. Một tiến trình như vậy được gọi là *tiến trình đệ quy tuyến tính*.

Ngược lại, tiến trình thứ hai không tăng và co lại. Ở mỗi bước, tất cả những gì chúng ta cần theo dõi, đối với bất kỳ $n$ nào, là các giá trị hiện tại của các biến `product`, `counter` và `max-count`. Chúng ta gọi đây là *tiến trình lặp*. Nói chung, một tiến trình lặp là một tiến trình mà trạng thái của nó có thể được tóm tắt bằng một số cố định các *biến trạng thái*, cùng với một quy tắc cố định mô tả cách các biến trạng thái nên được cập nhật khi tiến trình di chuyển từ trạng thái này sang trạng thái khác và một kiểm tra kết thúc (tùy chọn) chỉ định các điều kiện mà tiến trình nên kết thúc. Trong tính toán $n!$, số bước yêu cầu tăng tuyến tính với $n$. Một tiến trình như vậy được gọi là *tiến trình lặp tuyến tính*.

Sự tương phản giữa hai tiến trình có thể được thấy theo một cách khác. Trong trường hợp lặp, các biến chương trình cung cấp một mô tả đầy đủ về trạng thái của tiến trình tại bất kỳ thời điểm nào. Nếu chúng ta dừng quá trình tính toán giữa các bước, tất cả những gì chúng ta cần làm để tiếp tục tính toán là cung cấp cho trình thông dịch các giá trị của ba biến chương trình. Không phải vậy với tiến trình đệ quy. Trong trường hợp này, có một số thông tin "ẩn" bổ sung, được duy trì bởi trình thông dịch và không có trong các biến chương trình, cho biết "tiến trình đang ở đâu" trong việc thương lượng chuỗi các thao tác bị trì hoãn. Chuỗi càng dài, càng phải duy trì nhiều thông tin.^[Khi chúng ta thảo luận về việc triển khai các thủ tục trên các máy thanh ghi trong [Chương 5](Chapter-5.xhtml#Chapter-5), chúng ta sẽ thấy rằng bất kỳ tiến trình lặp nào cũng có thể được hiện thực hóa "trong phần cứng" dưới dạng một máy có một tập hợp các thanh ghi cố định và không có bộ nhớ phụ trợ. Ngược lại, việc hiện thực hóa một tiến trình đệ quy đòi hỏi một máy sử dụng một cấu trúc dữ liệu phụ trợ được gọi là *stack*.]

Khi so sánh sự lặp và đệ quy, chúng ta phải cẩn thận để không nhầm lẫn khái niệm *tiến trình* đệ quy với khái niệm *thủ tục* đệ quy. Khi chúng ta mô tả một thủ tục là đệ quy, chúng ta đang đề cập đến một thực tế cú pháp là định nghĩa thủ tục đề cập (trực tiếp hoặc gián tiếp) đến chính thủ tục đó. Nhưng khi chúng ta mô tả một tiến trình tuân theo một mẫu, ví dụ, đệ quy tuyến tính, chúng ta đang nói về cách tiến trình phát triển, không phải về cú pháp của cách một thủ tục được viết. Có vẻ đáng lo ngại khi chúng ta gọi một thủ tục đệ quy như `fact-iter` là tạo ra một tiến trình lặp. Tuy nhiên, tiến trình thực sự là lặp: Trạng thái của nó được nắm bắt hoàn toàn bởi ba biến trạng thái của nó và một trình thông dịch chỉ cần theo dõi ba biến để thực thi tiến trình.

Một lý do khiến sự phân biệt giữa tiến trình và thủ tục có thể gây nhầm lẫn là hầu hết các triển khai của các ngôn ngữ phổ biến (bao gồm Ada, Pascal và C) được thiết kế theo cách mà việc diễn giải bất kỳ thủ tục đệ quy nào sẽ tiêu thụ một lượng bộ nhớ tăng lên cùng với số lượng cuộc gọi thủ tục, ngay cả khi tiến trình được mô tả, về nguyên tắc, là lặp. Do đó, các ngôn ngữ này chỉ có thể mô tả các tiến trình lặp bằng cách sử dụng các "cấu trúc vòng lặp" chuyên dụng như `do`, `repeat`, `until`, `for` và `while`. Việc triển khai Scheme mà chúng ta sẽ xem xét trong [Chương 5](Chapter-5.xhtml#Chapter-5) không có nhược điểm này. Nó sẽ thực thi một tiến trình lặp trong không gian không đổi, ngay cả khi tiến trình lặp được mô tả bằng một thủ tục đệ quy. Một triển khai có thuộc tính này được gọi là *đệ quy đuôi*. Với một triển khai đệ quy đuôi, sự lặp có thể được biểu thị bằng cơ chế gọi thủ tục thông thường, do đó các cấu trúc lặp đặc biệt chỉ hữu ích như một cú pháp đường.^[Đệ quy đuôi từ lâu đã được biết đến như một thủ thuật tối ưu hóa trình biên dịch. Cơ sở ngữ nghĩa mạch lạc cho đệ quy đuôi đã được cung cấp bởi Carl [Hewitt (1977)](References.xhtml#Hewitt-_00281977_0029), người đã giải thích nó theo mô hình "truyền thông điệp" của tính toán mà chúng ta sẽ thảo luận trong [Chương 3](Chapter-3.xhtml#Chapter-3). Lấy cảm hứng từ điều này, Gerald Jay Sussman và Guy Lewis Steele Jr. (xem [Steele và Sussman 1975](References.xhtml#Steele-and-Sussman-1975)) đã xây dựng một trình thông dịch đệ quy đuôi cho Scheme. Steele sau đó đã chỉ ra cách đệ quy đuôi là một hệ quả của cách tự nhiên để biên dịch các lệnh gọi thủ tục ([Steele 1977](References.xhtml#Steele-1977)). Tiêu chuẩn IEEE cho Scheme yêu cầu các triển khai Scheme phải là đệ quy đuôi.]

**Bài tập 1.9:** Mỗi thủ tục sau đây định nghĩa một phương pháp để cộng hai số nguyên dương theo các thủ tục `inc`, làm tăng đối số của nó lên 1 và `dec`, làm giảm đối số của nó đi 1.

``` {.scheme}
(define (+ a b)
  (if (= a 0) 
      b 
      (inc (+ (dec a) b))))

(define (+ a b)
  (if (= a 0) 
      b 
      (+ (dec a) (inc b))))
```

Sử dụng mô hình thay thế, minh họa tiến trình được tạo bởi mỗi thủ tục trong việc đánh giá `(+ 4 5)`. Các tiến trình này là lặp hay đệ quy?

**Bài tập 1.10:** Thủ tục sau tính một hàm toán học gọi là hàm Ackermann.

``` {.scheme}
(define (A x y)
  (cond ((= y 0) 0)
        ((= x 0) (* 2 y))
        ((= y 1) 2)
        (else (A (- x 1)
                 (A x (- y 1))))))
```

Các giá trị của các biểu thức sau là gì?

``` {.scheme}
(A 1 10)
(A 2 4)
(A 3 3)
```

Xem xét các thủ tục sau, trong đó `A` là thủ tục được định nghĩa ở trên:

``` {.scheme}
(define (f n) (A 0 n))
(define (g n) (A 1 n))
(define (h n) (A 2 n))
(define (k n) (* 5 n n))
```

Đưa ra các định nghĩa toán học ngắn gọn cho các hàm được tính bởi các thủ tục `f`, `g` và `h` cho các giá trị số nguyên dương của $n$. Ví dụ: `(k n)` tính $5n^{2}$.

## 1.2.2 Đệ Quy Cây

Một mẫu tính toán phổ biến khác được gọi là *đệ quy cây*. Ví dụ, hãy xem xét việc tính dãy số Fibonacci, trong đó mỗi số là tổng của hai số đứng trước:

0, 1, 1, 2, 3, 5, 8, 13, 21, ….

Nói chung, các số Fibonacci có thể được định nghĩa bằng quy tắc

$$\text{Fib}(n)\; = \;\begin{cases}
0 & {\;\text{if}\;\; n = 0,} \\
1 & {\;\text{if}\;\; n = 1,} \\
{\text{Fib}(n - 1) + \text{Fib}(n - 2)} & {\;\text{otherwise}.} \\
\end{cases}$$

Chúng ta có thể ngay lập tức chuyển định nghĩa này thành một thủ tục đệ quy để tính các số Fibonacci:

``` {.scheme}
(define (fib n)
  (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib (- n 1))
                 (fib (- n 2))))))
```

Hãy xem xét mô hình tính toán này. Để tính `(fib 5)`, chúng ta tính `(fib 4)` và `(fib 3)`. Để tính `(fib 4)`, chúng ta tính `(fib 3)` và `(fib 2)`. Nói chung, tiến trình phát triển trông giống như một cây, như được hiển thị trong [Hình 1.5](#Hình-1_002e5). Lưu ý rằng các nhánh chia thành hai ở mỗi cấp (ngoại trừ ở dưới cùng); điều này phản ánh thực tế là thủ tục `fib` tự gọi hai lần mỗi khi nó được gọi.

![](fig/chap1/Fig1.5d.std.svg 696.84x434.16)
**Hình 1.5:** Tiến trình đệ quy cây được tạo ra khi tính `(fib 5)`.

Thủ tục này mang tính hướng dẫn như một nguyên mẫu đệ quy cây, nhưng đây là một cách tồi tệ để tính các số Fibonacci vì nó thực hiện quá nhiều phép tính dư thừa. Lưu ý trong [Hình 1.5](#Hình-1_002e5) rằng toàn bộ phép tính của `(fib 3)` — gần một nửa công việc — bị trùng lặp. Trên thực tế, không khó để chỉ ra rằng số lần thủ tục sẽ tính `(fib 1)` hoặc `(fib 0)` (số lượng lá trong cây ở trên, nói chung) chính xác là $\text{Fib}(n + 1)$. Để có ý tưởng về mức độ tồi tệ của việc này, người ta có thể chỉ ra rằng giá trị của $\text{Fib}(n)$ tăng theo cấp số nhân với $n$. Chính xác hơn (xem [Bài tập 1.13](#Bài-tập-1_002e13)), $\text{Fib}(n)$ là số nguyên gần nhất với $\varphi^{n}/\sqrt{5}$, trong đó

$$\varphi\, = \,\frac{1 + \sqrt{5}}{2}\, \approx \, 1.6180$$

là *tỷ lệ vàng*, thỏa mãn phương trình

$$\varphi^{2}\, = \,{\varphi + 1.}$$

Như vậy, tiến trình sử dụng một số bước tăng theo cấp số nhân với đầu vào. Mặt khác, không gian yêu cầu chỉ tăng tuyến tính với đầu vào, vì chúng ta chỉ cần theo dõi các nút nằm trên chúng ta trong cây tại bất kỳ thời điểm nào trong quá trình tính toán. Nói chung, số lượng các bước cần thiết bởi một tiến trình đệ quy cây sẽ tỷ lệ với số lượng các nút trong cây, trong khi không gian yêu cầu sẽ tỷ lệ với độ sâu tối đa của cây.

Chúng ta cũng có thể xây dựng một tiến trình lặp để tính các số Fibonacci. Ý tưởng là sử dụng một cặp số nguyên $a$ và $b$, được khởi tạo thành $\text{Fib(1)\ =\ 1}$ và $\text{Fib(0)\ =\ 0}$, và lặp lại các phép biến đổi đồng thời

$$\begin{array}{l}
{a\;\leftarrow\; a + b,} \\
{b\;\leftarrow\; a.} \\
\end{array}$$

Không khó để chỉ ra rằng, sau khi áp dụng phép biến đổi này $n$ lần, $a$ và $b$ sẽ lần lượt bằng $\text{Fib}(n + 1)$ và $\text{Fib}(n)$. Vì vậy, chúng ta có thể tính các số Fibonacci lặp đi lặp lại bằng thủ tục

``` {.scheme}
(define (fib n) 
  (fib-iter 1 0 n))

(define (fib-iter a b count)
  (if (= count 0)
      b
      (fib-iter (+ a b) a (- count 1))))
```

Phương pháp thứ hai này để tính $\text{Fib}(n)$ là một phép lặp tuyến tính. Sự khác biệt về số bước yêu cầu của hai phương pháp — một tuyến tính theo $n$, một tăng nhanh như chính $\text{Fib}(n)$ — là rất lớn, ngay cả đối với đầu vào nhỏ.

Người ta không nên kết luận từ điều này rằng các tiến trình đệ quy cây là vô dụng. Khi chúng ta xem xét các tiến trình hoạt động trên dữ liệu có cấu trúc phân cấp thay vì các số, chúng ta sẽ thấy rằng đệ quy cây là một công cụ tự nhiên và mạnh mẽ.^[Một ví dụ về điều này đã được gợi ý trong [1.1.3](1_002e1.xhtml#g_t1_002e1_002e3). Bản thân trình thông dịch đánh giá các biểu thức bằng cách sử dụng một tiến trình đệ quy cây.] Nhưng ngay cả trong các phép toán số, các tiến trình đệ quy cây có thể hữu ích trong việc giúp chúng ta hiểu và thiết kế các chương trình. Ví dụ, mặc dù thủ tục `fib` đầu tiên kém hiệu quả hơn nhiều so với thủ tục thứ hai, nhưng nó đơn giản hơn, không khác gì một bản dịch sang Lisp của định nghĩa dãy Fibonacci. Để xây dựng thuật toán lặp, cần lưu ý rằng phép tính có thể được diễn giải lại thành một phép lặp với ba biến trạng thái.

### Ví dụ: Đếm sự thay đổi

Chỉ cần một chút khéo léo để đưa ra thuật toán Fibonacci lặp. Ngược lại, hãy xem xét vấn đề sau: Có bao nhiêu cách khác nhau chúng ta có thể đổi 1,00 đô la, với nửa đô la, một phần tư, một phần mười, đồng năm xu và đồng xu? Tổng quát hơn, chúng ta có thể viết một thủ tục để tính số cách đổi bất kỳ số tiền nào không?

Vấn đề này có một giải pháp đơn giản dưới dạng một thủ tục đệ quy. Giả sử chúng ta nghĩ các loại tiền xu có sẵn được sắp xếp theo một thứ tự nào đó. Sau đó, mối quan hệ sau đây được giữ:

Số cách đổi số tiền $a$ bằng cách sử dụng $n$ loại tiền xu bằng

- số cách đổi số tiền $a$ bằng cách sử dụng tất cả các loại tiền xu ngoại trừ loại đầu tiên, cộng với
- số cách đổi số tiền $a - d$ bằng cách sử dụng tất cả $n$ loại tiền xu, trong đó $d$ là mệnh giá của loại tiền xu đầu tiên.

Để xem tại sao điều này là đúng, hãy quan sát rằng các cách thay đổi có thể được chia thành hai nhóm: những cách không sử dụng bất kỳ loại tiền xu nào đầu tiên và những cách sử dụng. Do đó, tổng số cách để thay đổi một số tiền nào đó bằng số cách để thay đổi số tiền mà không cần sử dụng bất kỳ loại tiền xu nào đầu tiên, cộng với số cách thay đổi giả sử rằng chúng ta sử dụng loại tiền xu đầu tiên. Nhưng số thứ hai bằng số cách thay đổi số tiền còn lại sau khi sử dụng một đồng xu thuộc loại đầu tiên.

Do đó, chúng ta có thể giảm đệ quy bài toán thay đổi một số tiền nhất định thành bài toán thay đổi các số tiền nhỏ hơn bằng cách sử dụng ít loại tiền xu hơn. Hãy xem xét cẩn thận quy tắc giảm này và tự thuyết phục rằng chúng ta có thể sử dụng nó để mô tả một thuật toán nếu chúng ta chỉ định các trường hợp suy biến sau:^[Ví dụ: hãy xem chi tiết cách quy tắc giảm được áp dụng cho bài toán thay đổi 10 xu bằng đồng xu và đồng năm xu.]

- Nếu $a$ chính xác bằng 0, chúng ta nên tính đó là 1 cách để thay đổi.
- Nếu $a$ nhỏ hơn 0, chúng ta nên tính đó là 0 cách để thay đổi.
- Nếu $n$ là 0, chúng ta nên tính đó là 0 cách để thay đổi.

Chúng ta có thể dễ dàng chuyển mô tả này thành một thủ tục đệ quy:

``` {.scheme}
(define (count-change amount)
  (cc amount 5))

(define (cc amount kinds-of-coins)
  (cond ((= amount 0) 1)
        ((or (< amount 0) 
             (= kinds-of-coins 0)) 
         0)
        (else 
         (+ (cc amount (- kinds-of-coins 1))
            (cc (- amount (first-denomination 
                           kinds-of-coins))
                kinds-of-coins)))))

(define (first-denomination kinds-of-coins)
  (cond ((= kinds-of-coins 1) 1)
        ((= kinds-of-coins 2) 5)
        ((= kinds-of-coins 3) 10)
        ((= kinds-of-coins 4) 25)
        ((= kinds-of-coins 5) 50)))
```

(Thủ tục `first-denomination` lấy đầu vào là số loại tiền xu có sẵn và trả về mệnh giá của loại đầu tiên. Ở đây, chúng ta đang nghĩ về các đồng xu được sắp xếp theo thứ tự từ lớn nhất đến nhỏ nhất, nhưng bất kỳ thứ tự nào cũng sẽ phù hợp.) Bây giờ chúng ta có thể trả lời câu hỏi ban đầu của mình về việc đổi một đô la:

``` {.scheme}
(count-change 100)
292
```

`Count-change` tạo ra một tiến trình đệ quy cây với sự dư thừa tương tự như trong lần triển khai đầu tiên của chúng ta về `fib`. (Sẽ mất khá nhiều thời gian để tính được 292.) Mặt khác, không rõ làm thế nào để thiết kế một thuật toán tốt hơn để tính kết quả và chúng ta để vấn đề này như một thử thách. Quan sát rằng một tiến trình đệ quy cây có thể rất kém hiệu quả nhưng thường dễ dàng chỉ định và hiểu đã khiến mọi người đề xuất rằng người ta có thể đạt được những điều tốt nhất của cả hai thế giới bằng cách thiết kế một "trình biên dịch thông minh" có thể chuyển đổi các thủ tục đệ quy cây thành các thủ tục hiệu quả hơn tính cùng một kết quả.^[Một cách để đối phó với các phép tính dư thừa là sắp xếp các vấn đề để chúng ta tự động xây dựng một bảng các giá trị khi chúng được tính toán. Mỗi khi chúng ta được yêu cầu áp dụng thủ tục cho một số đối số, trước tiên chúng ta xem xét xem giá trị đã được lưu trữ trong bảng chưa, trong trường hợp đó, chúng ta tránh thực hiện phép tính dư thừa. Chiến lược này, được gọi là *bảng* hoặc *ghi nhớ*, có thể được triển khai một cách đơn giản. Bảng đôi khi có thể được sử dụng để chuyển đổi các tiến trình yêu cầu một số bước theo cấp số nhân (chẳng hạn như `count-change`) thành các tiến trình mà các yêu cầu về không gian và thời gian tăng tuyến tính theo đầu vào. Xem [Bài tập 3.27](3_002e3.xhtml#Bài-tập-3_002e27).]

**Bài tập 1.11:** Một hàm $f$ được định nghĩa theo quy tắc $f(n) = n$ nếu $n < 3$ và ${f(n)} = {f(n - 1)} + {2f(n - 2)} + {3f(n - 3)}$ nếu $n \geq 3$. Viết một thủ tục tính $f$ bằng một tiến trình đệ quy. Viết một thủ tục tính $f$ bằng một tiến trình lặp.

**Bài tập 1.12:** Mô hình số sau được gọi là *tam giác Pascal*.

``` {.example}
         1
       1   1
     1   2   1
   1   3   3   1
 1   4   6   4   1
       . . .
```

Các số ở cạnh của tam giác đều là 1 và mỗi số bên trong tam giác là tổng của hai số ở trên nó.^[Các phần tử của tam giác Pascal được gọi là *hệ số nhị thức*, vì hàng thứ $n$ bao gồm các hệ số của các số hạng trong khai triển của $(x + y)^{n}$. Mô hình tính toán các hệ số này đã xuất hiện trong công trình mang tính bước ngoặt năm 1653 của Blaise Pascal về lý thuyết xác suất, Traité du triangle arithmétique. Theo [Knuth (1973)](References.xhtml#Knuth-_00281973_0029), cùng một mô hình xuất hiện trong Szu-yuen Yü-chien (“Tấm gương quý giá của bốn yếu tố”), được xuất bản bởi nhà toán học Trung Quốc Chu Thế Kiệt năm 1303, trong các tác phẩm của nhà thơ và nhà toán học người Ba Tư thế kỷ thứ mười hai Omar Khayyam, và trong các tác phẩm của nhà toán học người Hindu thế kỷ thứ mười hai Bháscara Áchárya.] Viết một thủ tục tính các phần tử của tam giác Pascal bằng một tiến trình đệ quy.

**Bài tập 1.13:** Chứng minh rằng $\text{Fib}(n)$ là số nguyên gần nhất với $\varphi^{n}/\sqrt{5}$, trong đó $\varphi = {(1 + \sqrt{5})/2}$. Gợi ý: Đặt $\psi = {(1 - \sqrt{5})/2}$. Sử dụng quy nạp và định nghĩa của các số Fibonacci (xem [1.2.2](#g_t1_002e2_002e2)) để chứng minh rằng ${\text{Fib}(n)} = {(\varphi^{n} - \psi^{n})/\sqrt{5}}$.

## 1.2.3 Cấp Độ Tăng Trưởng

Các ví dụ trước đây minh họa rằng các tiến trình có thể khác nhau đáng kể về tốc độ tiêu thụ tài nguyên tính toán. Một cách thuận tiện để mô tả sự khác biệt này là sử dụng khái niệm *cấp độ tăng trưởng* để có được thước đo thô về tài nguyên mà một tiến trình yêu cầu khi các đầu vào trở nên lớn hơn.

Giả sử $n$ là một tham số đo lường kích thước của bài toán và $R(n)$ là lượng tài nguyên mà tiến trình yêu cầu đối với một bài toán có kích thước $n$. Trong các ví dụ trước của chúng ta, chúng ta đã lấy $n$ làm số mà một hàm nhất định sẽ được tính, nhưng có các khả năng khác. Ví dụ, nếu mục tiêu của chúng ta là tính một phép xấp xỉ căn bậc hai của một số, chúng ta có thể lấy $n$ là số chữ số chính xác cần thiết. Đối với phép nhân ma trận, chúng ta có thể lấy $n$ là số hàng trong ma trận. Nói chung, có một số thuộc tính của bài toán mà đối với chúng, người ta sẽ mong muốn phân tích một tiến trình nhất định. Tương tự, $R(n)$ có thể đo số lượng thanh ghi lưu trữ bên trong được sử dụng, số lượng thao tác máy cơ bản được thực hiện, v.v. Trong các máy tính chỉ thực hiện một số thao tác cố định tại một thời điểm, thời gian cần thiết sẽ tỷ lệ với số lượng thao tác máy cơ bản được thực hiện.

Chúng ta nói rằng $R(n)$ có cấp độ tăng trưởng $\Theta(f(n))$, được viết là ${R(n)} = {\Theta(f(n))}$ (phát âm là "theta của $f(n)$"), nếu có các hằng số dương $k_{1}$ và $k_{2}$ độc lập với $n$ sao cho ${k_{1}f(n)} \leq {R(n)} \leq {k_{2}f(n)}$ đối với bất kỳ giá trị đủ lớn nào của $n$. (Nói cách khác, đối với $n$ lớn, giá trị $R(n)$ được kẹp giữa $k_{1}f(n)$ và $k_{2}f(n)$.)

Ví dụ, với tiến trình đệ quy tuyến tính để tính giai thừa được mô tả trong [1.2.1](#g_t1_002e2_002e1), số bước tăng tỷ lệ với đầu vào $n$. Do đó, các bước cần thiết cho tiến trình này tăng lên là $\Theta(n)$. Chúng ta cũng thấy rằng không gian yêu cầu tăng lên là $\Theta(n)$. Đối với giai thừa lặp, số bước vẫn là $\Theta(n)$ nhưng không gian là $\Theta(1)$ — tức là hằng số.^[Những phát biểu này che giấu rất nhiều sự đơn giản hóa quá mức. Ví dụ, nếu chúng ta tính các bước tiến trình là "thao tác máy", chúng ta đang đưa ra giả định rằng số lượng thao tác máy cần thiết để thực hiện, chẳng hạn, một phép nhân là độc lập với kích thước của các số được nhân, điều này là sai nếu các số đủ lớn. Các nhận xét tương tự cũng đúng đối với ước tính không gian. Giống như việc thiết kế và mô tả một tiến trình, việc phân tích một tiến trình có thể được thực hiện ở các cấp độ trừu tượng khác nhau.] Phép tính Fibonacci đệ quy cây yêu cầu $\Theta(\varphi^{n})$ bước và không gian $\Theta(n)$, trong đó $\varphi$ là tỷ lệ vàng được mô tả trong [1.2.2](#g_t1_002e2_002e2).

Cấp độ tăng trưởng chỉ cung cấp một mô tả thô sơ về hành vi của một tiến trình. Ví dụ: một tiến trình yêu cầu $n^{2}$ bước và một tiến trình yêu cầu $1000n^{2}$ bước và một tiến trình yêu cầu ${3n^{2}} + {10n} + 17$ bước đều có cấp độ tăng trưởng $\Theta(n^{2})$. Mặt khác, cấp độ tăng trưởng cung cấp một dấu hiệu hữu ích về cách chúng ta có thể mong đợi hành vi của tiến trình thay đổi khi chúng ta thay đổi kích thước của bài toán. Đối với một tiến trình $\Theta(n)$ (tuyến tính), việc tăng gấp đôi kích thước sẽ làm tăng gấp đôi lượng tài nguyên được sử dụng. Đối với một tiến trình theo cấp số nhân, mỗi mức tăng về kích thước bài toán sẽ nhân việc sử dụng tài nguyên với một hệ số không đổi. Trong phần còn lại của [1.2](#g_t1_002e2), chúng ta sẽ xem xét hai thuật toán có cấp độ tăng trưởng là logarit, sao cho việc tăng gấp đôi kích thước bài toán sẽ làm tăng yêu cầu tài nguyên thêm một lượng không đổi.

**Bài tập 1.14:** Vẽ cây minh họa tiến trình được tạo bởi thủ tục `count-change` của [1.2.2](#g_t1_002e2_002e2) khi thay đổi 11 xu. Các cấp độ tăng trưởng của không gian và số bước được sử dụng bởi tiến trình này khi số tiền cần thay đổi tăng lên là bao nhiêu?

**Bài tập 1.15:** Sin của một góc (được chỉ định bằng radian) có thể được tính bằng cách sử dụng phép xấp xỉ $\sin x \approx x$ nếu $x$ đủ nhỏ và định thức lượng giác

$${\sin x}\, = \,{3\sin\frac{x}{3}}\, - \,{4\sin^{3}\frac{x}{3}}$$

để giảm kích thước của đối số sin. (Đối với mục đích của bài tập này, một góc được coi là "đủ nhỏ" nếu độ lớn của nó không lớn hơn 0,1 radian.) Các ý tưởng này được kết hợp trong các thủ tục sau:

``` {.scheme}
(define (cube x) (* x x x))
(define (p x) (- (* 3 x) (* 4 (cube x))))
(define (sine angle)
   (if (not (> (abs angle) 0.1))
       angle
       (p (sine (/ angle 3.0)))))
```

1. Thủ tục `p` được áp dụng bao nhiêu lần khi `(sine 12.15)` được đánh giá