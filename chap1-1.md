# 1.1 Các Yếu Tố Của Lập Trình

Một ngôn ngữ lập trình mạnh mẽ hơn là chỉ một phương tiện để hướng dẫn máy tính thực hiện các tác vụ. Ngôn ngữ này còn đóng vai trò như một khuôn khổ để chúng ta tổ chức các ý tưởng về các quy trình. Do đó, khi mô tả một ngôn ngữ, chúng ta cần chú ý đặc biệt đến các phương tiện mà ngôn ngữ đó cung cấp để kết hợp các ý tưởng đơn giản thành các ý tưởng phức tạp hơn. Mọi ngôn ngữ mạnh mẽ đều có ba cơ chế để đạt được điều này:

- **biểu thức nguyên thủy**, đại diện cho các thực thể đơn giản nhất mà ngôn ngữ quan tâm,
- **phương tiện kết hợp**, bằng cách xây dựng các thành phần phức hợp từ các thành phần đơn giản hơn, và
- **phương tiện trừu tượng hóa**, bằng cách đặt tên và thao tác các thành phần phức hợp như các đơn vị.

Trong lập trình, chúng ta xử lý hai loại yếu tố: thủ tục và dữ liệu. (Sau này chúng ta sẽ phát hiện ra rằng chúng thực sự không quá khác biệt.) Về mặt không chính thức, dữ liệu là “vật chất” mà chúng ta muốn thao tác, và thủ tục là các mô tả về các quy tắc để thao tác dữ liệu. Do đó, bất kỳ ngôn ngữ lập trình mạnh mẽ nào cũng nên có khả năng mô tả dữ liệu nguyên thủy và thủ tục nguyên thủy và nên có các phương pháp kết hợp và trừu tượng hóa thủ tục và dữ liệu.

Trong chương này, chúng ta sẽ chỉ xử lý dữ liệu số học đơn giản để có thể tập trung vào các quy tắc để xây dựng thủ tục.^[Cách mô tả số là “dữ liệu đơn giản” là một sự nói dối trắng trợn. Trên thực tế, cách xử lý số là một trong những khía cạnh khó khăn và gây nhầm lẫn nhất của bất kỳ ngôn ngữ lập trình nào. Một số vấn đề điển hình liên quan là: Một số hệ thống máy tính phân biệt *số nguyên*, như 2, với *số thực*, như 2,71. Liệu số thực 2,00 có khác với số nguyên 2 không? Các phép toán số học được sử dụng cho số nguyên có giống với các phép toán được sử dụng cho số thực không? 6 chia cho 2 có cho kết quả là 3, hay 3,0 không? Số lớn nhất mà chúng ta có thể biểu diễn là bao nhiêu? Chúng ta có thể biểu diễn bao nhiêu chữ số thập phân chính xác? Phạm vi của các số nguyên có giống với phạm vi của số thực không? Bên trên những câu hỏi này, tất nhiên, là một tập hợp các vấn đề liên quan đến lỗi làm tròn và cắt xén – toàn bộ khoa học về phân tích số. Vì trọng tâm của cuốn sách này là thiết kế chương trình quy mô lớn hơn là kỹ thuật số, chúng ta sẽ bỏ qua những vấn đề này. Các ví dụ số trong chương này sẽ thể hiện hành vi làm tròn thông thường mà người ta quan sát được khi sử dụng các phép toán số học bảo toàn một số hữu hạn các chữ số thập phân chính xác trong các phép toán không phải là số nguyên.] Trong các chương sau, chúng ta sẽ thấy rằng những quy tắc này cũng cho phép chúng ta xây dựng các thủ tục để thao tác dữ liệu phức hợp.


## 1.1.1 Biểu Thức

Một cách dễ dàng để bắt đầu lập trình là xem xét một số tương tác điển hình với trình thông dịch cho phương ngữ Scheme của Lisp. Hãy tưởng tượng bạn đang ngồi trước một thiết bị đầu cuối máy tính. Bạn nhập một *biểu thức*, và trình thông dịch trả lời bằng cách hiển thị kết quả của việc *đánh giá* biểu thức đó.

Một loại biểu thức nguyên thủy mà bạn có thể nhập là một số. (Cụ thể hơn, biểu thức mà bạn nhập bao gồm các số biểu diễn số đó trong hệ thập phân.) Nếu bạn đưa cho Lisp một số

``` {.scheme}
486
```

thì trình thông dịch sẽ trả lời bằng cách in^[Trong toàn bộ cuốn sách này, khi chúng ta muốn nhấn mạnh sự khác biệt giữa đầu vào được nhập bởi người dùng và phản hồi được in bởi trình thông dịch, chúng ta sẽ hiển thị phản hồi này bằng kiểu chữ nghiêng.]

``` {.scheme}
486
```

Các biểu thức đại diện cho số có thể được kết hợp với một biểu thức đại diện cho một thủ tục nguyên thủy (như `+` hoặc `*`) để tạo thành một biểu thức hợp chất đại diện cho việc áp dụng thủ tục cho các số đó. Ví dụ:

``` {.scheme}
(+ 137 349)
486

(- 1000 334)
666

(* 5 99)
495

(/ 10 5)
2

(+ 2.7 10)
12.7
```

Các biểu thức như vậy, được tạo thành bằng cách giới hạn một danh sách các biểu thức trong dấu ngoặc đơn để chỉ định việc áp dụng thủ tục, được gọi là *các kết hợp*. Thành phần bên trái nhất trong danh sách được gọi là *tác tử*, và các thành phần khác được gọi là *các toán hạng*. Giá trị của một kết hợp được thu được bằng cách áp dụng thủ tục được chỉ định bởi tác tử vào *các đối số* là giá trị của các toán hạng.

Quy ước đặt tác tử ở bên trái các toán hạng được gọi là *kiểu ký hiệu tiền tố*, và nó có thể hơi gây nhầm lẫn lúc đầu vì nó khác biệt đáng kể so với quy ước toán học thông thường. Tuy nhiên, ký hiệu tiền tố có một số ưu điểm. Một trong số đó là nó có thể chứa đựng các thủ tục có thể chấp nhận một số lượng tùy ý các đối số, như trong các ví dụ sau:

``` {.scheme}
(+ 21 35 12 7)
75

(* 25 4 12)
1200
```

Không thể có sự mơ hồ nào xảy ra, vì tác tử luôn luôn là thành phần bên trái nhất và toàn bộ kết hợp được giới hạn bởi dấu ngoặc đơn.

Ưu điểm thứ hai của ký hiệu tiền tố là nó mở rộng theo cách đơn giản để cho phép các kết hợp được *lồng nhau*, nghĩa là, có các kết hợp mà các thành phần của chúng là chính các kết hợp:

``` {.scheme}
(+ (* 3 5) (- 10 6))
19
```

Không có giới hạn (về nguyên tắc) độ sâu của việc lồng nhau như vậy và độ phức tạp tổng thể của các biểu thức mà trình thông dịch Lisp có thể đánh giá. Chính chúng ta, con người, là những người bị nhầm lẫn bởi các biểu thức còn tương đối đơn giản như

``` {.scheme}
(+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))
```

mà trình thông dịch sẽ dễ dàng đánh giá thành 57. Chúng ta có thể giúp chính mình bằng cách viết biểu thức như vậy ở dạng

``` {.scheme}
(+ (* 3
      (+ (* 2 4)
         (+ 3 5)))
   (+ (- 10 7)
      6))
```

theo quy ước định dạng được gọi là *định dạng đẹp*, trong đó mỗi kết hợp dài được viết sao cho các toán hạng được căn thẳng theo hàng dọc. Việc thụt lề kết quả hiển thị rõ ràng cấu trúc của biểu thức.^[Các hệ thống Lisp thường cung cấp các tính năng để hỗ trợ người dùng trong việc định dạng các biểu thức. Hai tính năng đặc biệt hữu ích là một tính năng tự động thụt lề vào vị trí định dạng đẹp thích hợp bất cứ khi nào bắt đầu một dòng mới và một tính năng làm nổi bật dấu ngoặc đơn khớp khi một dấu ngoặc đơn phải được nhập.]

Ngay cả với các biểu thức phức tạp, trình thông dịch luôn vận hành theo cùng một chu kỳ cơ bản: Đọc một biểu thức từ thiết bị đầu cuối, đánh giá biểu thức và in kết quả. Cách thức hoạt động này thường được diễn tả bằng cách nói rằng trình thông dịch chạy trong một *vòng lặp đọc-đánh giá-in*. Hãy đặc biệt quan sát rằng không cần hướng dẫn trình thông dịch một cách rõ ràng để in giá trị của biểu thức.^[Lisp tuân theo quy ước rằng mọi biểu thức đều có một giá trị. Quy ước này, cùng với danh tiếng cũ của Lisp là một ngôn ngữ không hiệu quả, là nguồn gốc của câu nói đùa của Alan Perlis (trích dẫn lại Oscar Wilde) rằng “các lập trình viên Lisp biết giá trị của mọi thứ nhưng không biết chi phí của bất cứ thứ gì.”]


## 1.1.2 Đặt Tên và Môi Trường

Một khía cạnh quan trọng của một ngôn ngữ lập trình là các phương tiện mà nó cung cấp để sử dụng tên để tham chiếu đến các đối tượng tính toán. Chúng ta nói rằng tên xác định một *biến* mà *giá trị* của nó là đối tượng.

Trong phương ngữ Scheme của Lisp, chúng ta đặt tên cho các thứ bằng `define`. Nhập

``` {.scheme}
(define size 2)
```

gây ra việc trình thông dịch liên kết giá trị 2 với tên `size`.^[Trong cuốn sách này, chúng ta không hiển thị phản hồi của trình thông dịch khi đánh giá các định nghĩa, vì điều này phụ thuộc rất nhiều vào việc thực hiện.] Sau khi tên `size` được liên kết với số 2, chúng ta có thể tham chiếu đến giá trị 2 bằng tên:

``` {.scheme}
size
2

(* 5 size)
10
```

Dưới đây là thêm một số ví dụ về việc sử dụng `define`:

``` {.scheme}
(define pi 3.14159)
(define radius 10)

(* pi (* radius radius))
314.159

(define circumference (* 2 pi radius))

circumference
62.8318
```

`Define` là phương tiện trừu tượng hóa đơn giản nhất của ngôn ngữ của chúng ta, vì nó cho phép chúng ta sử dụng các tên đơn giản để tham chiếu đến kết quả của các phép toán hợp chất, như `circumference` được tính toán ở trên. Nói chung, các đối tượng tính toán có thể có cấu trúc rất phức tạp, và việc phải ghi nhớ và lặp lại các chi tiết của chúng mỗi khi chúng ta muốn sử dụng chúng sẽ rất bất tiện. Thực tế, các chương trình phức tạp được xây dựng bằng cách xây dựng, từng bước một, các đối tượng tính toán có độ phức tạp ngày càng tăng. Trình thông dịch làm cho việc xây dựng chương trình từng bước này đặc biệt thuận tiện vì các mối liên hệ tên-đối tượng có thể được tạo dần dần trong các tương tác liên tiếp. Tính năng này khuyến khích việc phát triển và kiểm thử chương trình một cách tăng dần và phần lớn là nguyên nhân khiến một chương trình Lisp thường bao gồm một số lượng lớn các thủ tục tương đối đơn giản.

Rõ ràng là khả năng liên kết giá trị với các ký hiệu và sau đó truy xuất chúng có nghĩa là trình thông dịch phải duy trì một số loại bộ nhớ theo dõi các cặp tên-đối tượng. Bộ nhớ này được gọi là *môi trường* (cụ thể hơn là *môi trường toàn cục*, vì chúng ta sẽ thấy sau này rằng một phép tính có thể liên quan đến một số môi trường khác nhau).^[[Chương 3](Chapter-3.xhtml#Chapter-3) sẽ chỉ ra rằng khái niệm môi trường này rất quan trọng, cả cho việc hiểu cách trình thông dịch hoạt động và cho việc thực hiện các trình thông dịch.]


## 1.1.3 Đánh Giá Các Kết Hợp

Một trong những mục tiêu của chúng ta trong chương này là tách biệt các vấn đề về tư duy theo thủ tục. Ví dụ, hãy xem xét rằng, trong việc đánh giá các kết hợp, chính trình thông dịch đang tuân theo một thủ tục.

> Để đánh giá một kết hợp, hãy làm như sau:
> > 1. Đánh giá các biểu thức con của kết hợp.
> 2. Áp dụng thủ tục là giá trị của biểu thức con bên trái nhất (tác tử) vào các đối số là giá trị của các biểu thức con khác (các toán hạng).

Ngay cả quy tắc đơn giản này cũng minh họa một số điểm quan trọng về quy trình nói chung. Đầu tiên, hãy quan sát rằng bước đầu tiên chỉ định rằng để thực hiện quá trình đánh giá cho một kết hợp, chúng ta phải thực hiện quá trình đánh giá đối với mỗi phần tử của kết hợp. Do đó, quy tắc đánh giá có bản chất *đệ quy*; nghĩa là, nó bao gồm, như một trong những bước của nó, nhu cầu phải gọi lại chính quy tắc đó.^[Có vẻ kỳ lạ khi quy tắc đánh giá nói, như một phần của bước đầu tiên, rằng chúng ta nên đánh giá phần tử bên trái nhất của một kết hợp, vì lúc này nó chỉ có thể là một tác tử như `+` hoặc `*` đại diện cho một thủ tục nguyên thủy tích hợp như phép cộng hoặc phép nhân. Chúng ta sẽ thấy sau này rằng việc có thể làm việc với các kết hợp mà các tác tử của chúng là chính các biểu thức hợp chất là rất hữu ích.]

Hãy chú ý cách mà ý tưởng về đệ quy có thể được sử dụng một cách ngắn gọn để biểu đạt những gì, trong trường hợp kết hợp lồng sâu, nếu không sẽ được xem là một quy trình khá phức tạp. Ví dụ, việc đánh giá

``` {.scheme}
(* (+ 2 (* 4 6)) (+ 3 5 7))
```

yêu cầu quy tắc đánh giá được áp dụng cho bốn kết hợp khác nhau. Chúng ta có thể có được một hình ảnh của quá trình này bằng cách biểu diễn kết hợp dưới dạng một cây, như được hiển thị trong [Hình 1.1](#Hình-1_002e1). Mỗi kết hợp được biểu diễn bằng một nút với các nhánh tương ứng với tác tử và các toán hạng của kết hợp phát sinh từ nó. Các nút đầu cuối (nghĩa là các nút không có nhánh phát sinh từ chúng) đại diện cho hoặc các tác tử hoặc các số. Nhìn đánh giá theo cây, chúng ta có thể tưởng tượng rằng các giá trị của các toán hạng rỉ xuống phía trên, bắt đầu từ các nút đầu cuối và sau đó kết hợp ở các mức cao hơn. Nói chung, chúng ta sẽ thấy rằng đệ quy là một kỹ thuật rất mạnh mẽ để xử lý các đối tượng phân cấp, có dạng cây. Trên thực tế, dạng “rỉ xuống các giá trị phía trên” của quy tắc đánh giá là một ví dụ về một loại quy trình chung được gọi là *tích lũy cây*.

![](fig/chap1/Fig1.1g.std.svg)
**Hình 1.1:** Biểu diễn cây, hiển thị giá trị của mỗi kết hợp con.

Tiếp theo, hãy quan sát rằng việc áp dụng lặp đi lặp lại bước đầu tiên đưa chúng ta đến điểm mà chúng ta cần đánh giá, không phải là các kết hợp, mà là các biểu thức nguyên thủy như số, các tác tử tích hợp hoặc các tên khác. Chúng ta xử lý các trường hợp nguyên thủy bằng cách quy định rằng

- các giá trị của các số là các số mà chúng đặt tên,
- các giá trị của các tác tử tích hợp là các chuỗi hướng dẫn máy thực hiện các phép toán tương ứng, và
- các giá trị của các tên khác là các đối tượng được liên kết với các tên đó trong môi trường.

Chúng ta có thể coi quy tắc thứ hai là một trường hợp đặc biệt của quy tắc thứ ba bằng cách quy định rằng các ký hiệu như `+` và `*` cũng được bao gồm trong môi trường toàn cục và được liên kết với các chuỗi hướng dẫn máy là “giá trị” của chúng. Điểm chính cần lưu ý là vai trò của môi trường trong việc xác định ý nghĩa của các ký hiệu trong các biểu thức. Trong một ngôn ngữ tương tác như Lisp, việc nói về giá trị của một biểu thức như `(+ x 1)` là vô nghĩa nếu không chỉ định bất kỳ thông tin nào về môi trường sẽ cung cấp ý nghĩa cho ký hiệu `x` (hoặc ngay cả ký hiệu `+`). Như chúng ta sẽ thấy trong [Chương 3](Chapter-3.xhtml#Chapter-3), khái niệm môi trường tổng quát như cung cấp ngữ cảnh mà trong đó đánh giá diễn ra sẽ đóng một vai trò quan trọng trong việc hiểu việc thực thi chương trình của chúng ta.

Hãy chú ý rằng quy tắc đánh giá được đưa ra ở trên không xử lý các định nghĩa. Ví dụ, việc đánh giá `(define x 3)` không áp dụng `define` cho hai đối số, trong đó một đối số là giá trị của ký hiệu `x` và đối số còn lại là 3, vì mục đích của `define` chính xác là liên kết `x` với một giá trị. (Nghĩa là, `(define x 3)` không phải là một kết hợp.)

Các ngoại lệ đối với quy tắc đánh giá chung như vậy được gọi là *dạng đặc biệt*. `Define` là ví dụ duy nhất về dạng đặc biệt mà chúng ta đã thấy cho đến nay, nhưng chúng ta sẽ gặp các ví dụ khác trong thời gian tới. Mỗi dạng đặc biệt đều có quy tắc đánh giá riêng. Các loại biểu thức khác nhau (mỗi loại có quy tắc đánh giá tương ứng) cấu thành cú pháp của ngôn ngữ lập trình. So với hầu hết các ngôn ngữ lập trình khác, Lisp có một cú pháp rất đơn giản; nghĩa là, quy tắc đánh giá cho các biểu thức có thể được mô tả bằng một quy tắc chung đơn giản cùng với các quy tắc chuyên biệt cho một số lượng nhỏ các dạng đặc biệt.^[Các dạng cú pháp đặc biệt chỉ là các cấu trúc bề mặt thay thế thuận tiện cho những thứ có thể được viết theo các cách đồng nhất hơn đôi khi được gọi là *đường lắt léo cú pháp*, để sử dụng một cụm từ do Peter Landin đặt ra. So với người dùng các ngôn ngữ khác, các lập trình viên Lisp, theo quy tắc, ít quan tâm đến các vấn đề về cú pháp hơn. (Ngược lại, hãy xem bất kỳ tài liệu hướng dẫn Pascal nào và nhận thấy rằng tài liệu đó dành bao nhiêu phần cho việc mô tả cú pháp.) Sự coi thường cú pháp này một phần là do tính linh hoạt của Lisp, làm cho việc thay đổi cú pháp bề mặt trở nên dễ dàng, và một phần là do nhận xét rằng nhiều cấu trúc cú pháp “thuận tiện”, làm cho ngôn ngữ ít đồng nhất hơn, cuối cùng gây ra nhiều rắc rối hơn là giá trị của chúng khi chương trình trở nên lớn và phức tạp. Theo lời của Alan Perlis, “đường lắt léo cú pháp gây ra ung thư dấu chấm phẩy.”]


## 1.1.4 Thủ Tục Hợp Chất

Chúng ta đã xác định trong Lisp một số yếu tố phải xuất hiện trong bất kỳ ngôn ngữ lập trình mạnh mẽ nào:

- Số và các phép toán số học là dữ liệu nguyên thủy và thủ tục.
- Việc lồng các kết hợp cung cấp một phương tiện kết hợp các hoạt động.
- Các định nghĩa liên kết tên với giá trị cung cấp một phương tiện trừu tượng hóa hạn chế.

Bây giờ chúng ta sẽ tìm hiểu về *định nghĩa thủ tục*, một kỹ thuật trừu tượng hóa mạnh mẽ hơn nhiều để một thao tác hợp chất có thể được đặt tên và sau đó được tham chiếu như một đơn vị.

Chúng ta bắt đầu bằng cách xem xét cách diễn đạt ý tưởng về “bình phương”. Chúng ta có thể nói, “Để bình phương một cái gì đó, hãy nhân nó với chính nó.” Điều này được biểu diễn trong ngôn ngữ của chúng ta là

``` {.scheme}
(define (square x) (* x x))
```

Chúng ta có thể hiểu điều này theo cách sau:

``` {.example}
(define (square x)    (*       x       x))
  |      |      |      |       |       |
 Để bình phương một cái gì đó, hãy nhân nó với chính nó.
```

Chúng ta có một *thủ tục hợp chất*, được đặt tên là `square`. Thủ tục đại diện cho hoạt động nhân một cái gì đó với chính nó. Cái cần được nhân được đặt tên cục bộ là `x`, đóng vai trò tương tự như một đại từ trong ngôn ngữ tự nhiên. Việc đánh giá định nghĩa tạo ra thủ tục hợp chất này và liên kết nó với tên `square`.^[Hãy lưu ý rằng có hai hoạt động khác nhau được kết hợp ở đây: chúng ta đang tạo thủ tục và chúng ta đang đặt tên cho nó là `square`. Có thể, thực tế là quan trọng, để có thể tách biệt hai khái niệm này – tạo thủ tục mà không đặt tên cho chúng và đặt tên cho các thủ tục đã được tạo ra. Chúng ta sẽ thấy cách thực hiện điều này trong [1.3.2](1_002e3.xhtml#g_t1_002e3_002e2).]

Dạng tổng quát của một định nghĩa thủ tục là

``` {.scheme}
(define (⟨name⟩ ⟨tham số chính thức⟩) ⟨thân⟩)
```

`⟨name⟩` là một ký hiệu sẽ được liên kết với định nghĩa thủ tục trong môi trường.^[Trong suốt cuốn sách này, chúng ta sẽ mô tả cú pháp tổng quát của các biểu thức bằng cách sử dụng các ký hiệu in nghiêng được giới hạn bởi dấu ngoặc nhọn – ví dụ: `⟨name⟩` – để chỉ định các “khoang trống” trong biểu thức để điền vào khi thực sự sử dụng biểu thức đó.] `⟨tham số chính thức⟩` là các tên được sử dụng trong thân thủ tục để tham chiếu đến các đối số tương ứng của thủ tục. `⟨thân⟩` là một biểu thức sẽ tạo ra giá trị của việc áp dụng thủ tục khi các tham số chính thức được thay thế bằng các đối số thực tế mà thủ tục được áp dụng cho chúng.^[Nói chung, thân của thủ tục có thể là một chuỗi các biểu thức. Trong trường hợp này, trình thông dịch đánh giá mỗi biểu thức trong chuỗi theo thứ tự và trả về giá trị của biểu thức cuối cùng như giá trị của việc áp dụng thủ tục.] `⟨name⟩` và `⟨tham số chính thức⟩` được nhóm lại trong dấu ngoặc đơn, giống như chúng sẽ được trong một cuộc gọi thực sự đến thủ tục được định nghĩa.

Sau khi định nghĩa `square`, chúng ta có thể sử dụng nó:

``` {.scheme}
(square 21)
441

(square (+ 2 5))
49

(square (square 3))
81
```

Chúng ta cũng có thể sử dụng `square` như một khối xây dựng trong việc định nghĩa các thủ tục khác. Ví dụ, $x^{2} + y^{2}$ có thể được biểu diễn là

``` {.scheme}
(+ (square x) (square y))
```

Chúng ta có thể dễ dàng định nghĩa một thủ tục `sum-of-squares` nhận hai số bất kỳ làm đối số và tạo ra tổng các bình phương của chúng:

``` {.scheme}
(define (sum-of-squares x y)
  (+ (square x) (square y)))

(sum-of-squares 3 4)
25
```

Bây giờ chúng ta có thể sử dụng `sum-of-squares` như một khối xây dựng để xây dựng các thủ tục hơn nữa:

``` {.scheme}
(define (f a)
  (sum-of-squares (+ a 1) (* a 2)))

(f 5)
136
```

Các thủ tục hợp chất được sử dụng theo đúng cách giống như các thủ tục nguyên thủy. Thực tế, người ta không thể nói được bằng cách nhìn vào định nghĩa của `sum-of-squares` được đưa ra ở trên liệu `square` có được tích hợp vào trình thông dịch hay không, giống như `+` và `*`, hoặc được định nghĩa là một thủ tục hợp chất.


## 1.1.5 Mô Hình Thay Thế Cho Việc Áp Dụng Thủ Tục

Để đánh giá một kết hợp mà tác tử đặt tên cho một thủ tục hợp chất, trình thông dịch thực hiện gần như cùng một quy trình như đối với các kết hợp mà các tác tử đặt tên cho các thủ tục nguyên thủy, mà chúng ta đã mô tả trong [1.1.3](#g_t1_002e1_002e3). Nghĩa là, trình thông dịch đánh giá các phần tử của kết hợp và áp dụng thủ tục (là giá trị của tác tử của kết hợp) vào các đối số (là giá trị của các toán hạng của kết hợp).

Chúng ta có thể giả định rằng cơ chế áp dụng các thủ tục nguyên thủy vào các đối số được tích hợp vào trình thông dịch. Đối với các thủ tục hợp chất, quá trình áp dụng như sau:

> Để áp dụng một thủ tục hợp chất cho các đối số, đánh giá thân thủ tục với mỗi tham số chính thức được thay thế bằng đối số tương ứng.

Để minh họa quá trình này, hãy đánh giá kết hợp

``` {.scheme}
(f 5)
```

trong đó `f` là thủ tục được định nghĩa trong [1.1.4](#g_t1_002e1_002e4). Chúng ta bắt đầu bằng cách lấy thân của `f`:

``` {.scheme}
(sum-of-squares (+ a 1) (* a 2))
```

Sau đó, chúng ta thay thế tham số chính thức `a` bằng đối số 5:

``` {.scheme}
(sum-of-squares (+ 5 1) (* 5 2))
```

Do đó, vấn đề được rút gọn thành việc đánh giá một kết hợp có hai toán hạng và một tác tử `sum-of-squares`. Việc đánh giá kết hợp này liên quan đến ba bài toán con. Chúng ta phải đánh giá tác tử để nhận được thủ tục cần áp dụng và chúng ta phải đánh giá các toán hạng để nhận được các đối số. Bây giờ `(+ 5 1)` cho ra 6 và `(* 5 2)` cho ra 10, vì vậy chúng ta phải áp dụng thủ tục `sum-of-squares` cho 6 và 10. Các giá trị này được thay thế cho các tham số chính thức `x` và `y` trong thân của `sum-of-squares`, làm giảm biểu thức thành

``` {.scheme}
(+ (square 6) (square 10))
```

Nếu chúng ta sử dụng định nghĩa của `square`, điều này sẽ được rút gọn thành

``` {.scheme}
(+ (* 6 6) (* 10 10))
```

và cuối cùng là

``` {.scheme}
136
```

Quá trình mà chúng ta vừa mô tả được gọi là *mô hình thay thế* cho việc áp dụng thủ tục. Nó có thể được coi như một mô hình xác định “ý nghĩa” của việc áp dụng thủ tục, về mặt các thủ tục trong chương này. Tuy nhiên, có hai điểm cần nhấn mạnh:

- Mục đích của việc thay thế là để giúp chúng ta suy nghĩ về việc áp dụng thủ tục, chứ không phải để cung cấp mô tả về cách thức trình thông dịch thực sự hoạt động. Các trình thông dịch điển hình không đánh giá các việc áp dụng thủ tục bằng cách thao tác văn bản của một thủ tục để thay thế các giá trị cho các tham số chính thức. Trong thực tế, việc “thay thế” được thực hiện bằng cách sử dụng một môi trường cục bộ cho các tham số chính thức. Chúng ta sẽ thảo luận điều này đầy đủ hơn trong [Chương 3](Chapter-3.xhtml#Chapter-3) và [Chương 4](Chapter-4.xhtml#Chapter-4) khi chúng ta kiểm tra việc thực hiện một trình thông dịch chi tiết.
- Trong suốt cuốn sách này, chúng ta sẽ trình bày một chuỗi các mô hình ngày càng tinh vi về cách thức trình thông dịch hoạt động, đạt đến việc thực hiện hoàn chỉnh một trình thông dịch và trình biên dịch trong [Chương 5](Chapter-5.xhtml#Chapter-5). Mô hình thay thế chỉ là mô hình đầu tiên trong số các mô hình này – một cách để bắt đầu suy nghĩ một cách chính thức về quá trình đánh giá. Nói chung, khi mô hình hóa các hiện tượng trong khoa học và kỹ thuật, chúng ta bắt đầu bằng các mô hình đơn giản hóa, không đầy đủ. Khi chúng ta xem xét các vấn đề chi tiết hơn, các mô hình đơn giản này trở nên không thích hợp và phải được thay thế bằng các mô hình tinh vi hơn. Mô hình thay thế cũng không ngoại lệ. Đặc biệt, khi chúng ta đề cập đến [Chương 3](Chapter-3.xhtml#Chapter-3) về việc sử dụng các thủ tục với “dữ liệu có thể thay đổi”, chúng ta sẽ thấy rằng mô hình thay thế bị phá vỡ và phải được thay thế bằng một mô hình phức tạp hơn của việc áp dụng thủ tục.^[Mặc dù ý tưởng thay thế rất đơn giản, hóa ra lại khá phức tạp để đưa ra một định nghĩa toán học chính xác về quá trình thay thế. Vấn đề phát sinh từ khả năng nhầm lẫn giữa các tên được sử dụng cho các tham số chính thức của một thủ tục và các tên (có thể giống hệt) được sử dụng trong các biểu thức mà thủ tục có thể được áp dụng. Thực tế, có một lịch sử dài về các định nghĩa sai về *thay thế* trong tài liệu về logic và ngữ nghĩa lập trình. Xem [Stoy 1977](References.xhtml#Stoy-1977) để thảo luận cẩn thận về việc thay thế.]


### Thứ tự áp dụng so với thứ tự bình thường

Theo mô tả về đánh giá được đưa ra trong [1.1.3](#g_t1_002e1_002e3), trình thông dịch đầu tiên đánh giá tác tử và các toán hạng, sau đó áp dụng thủ tục kết quả cho các đối số kết quả. Đây không phải là cách duy nhất để thực hiện đánh giá. Một mô hình đánh giá thay thế sẽ không đánh giá các toán hạng cho đến khi giá trị của chúng được cần thiết. Thay vào đó, nó sẽ thay thế các biểu thức toán hạng cho các tham số cho đến khi nó thu được một biểu thức chỉ liên quan đến các tác tử nguyên thủy, và sau đó thực hiện đánh giá. Nếu chúng ta sử dụng phương pháp này, việc đánh giá `(f 5)` sẽ diễn ra theo trình tự mở rộng

``` {.scheme}
(sum-of-squares (+ 5 1) (* 5 2))

(+ (square (+ 5 1)) 
   (square (* 5 2)))

(+ (* (+ 5 1) (+ 5 1)) 
   (* (* 5 2) (* 5 2)))
```

Theo sau đó là việc giảm

``` {.scheme}
(+ (* 6 6) 
   (* 10 10))

(+ 36 100)

136
```

Điều này cho cùng một kết quả như mô hình đánh giá trước đó của chúng ta, nhưng quá trình khác nhau. Đặc biệt, các đánh giá `(+ 5 1)` và `(* 5 2)` mỗi lần được thực hiện hai lần ở đây, tương ứng với việc giảm biểu thức `(* x x)` với `x` thay thế lần lượt bằng `(+ 5 1)` và `(* 5 2)`.

Phương pháp đánh giá “mở rộng hoàn toàn rồi giảm” thay thế này được gọi là *đánh giá bình thường*, trái ngược với phương pháp “đánh giá các đối số rồi áp dụng” mà trình thông dịch thực sự sử dụng, được gọi là *đánh giá theo thứ tự áp dụng*. Có thể chứng minh rằng, đối với các việc áp dụng thủ tục có thể được mô hình hóa bằng cách thay thế (bao gồm tất cả các thủ tục trong hai chương đầu tiên của cuốn sách này) và tạo ra các giá trị hợp lệ, việc đánh giá theo thứ tự bình thường và việc đánh giá theo thứ tự áp dụng tạo ra cùng một giá trị. (Xem [Bài tập 1.5](#Bài tập-1_002e5) cho một ví dụ về giá trị “không hợp lệ” mà việc đánh giá theo thứ tự bình thường và việc đánh giá theo thứ tự áp dụng không cho cùng một kết quả.)

Lisp sử dụng đánh giá theo thứ tự áp dụng, một phần là do hiệu quả bổ sung thu được từ việc tránh đánh giá nhiều lần các biểu thức như những biểu thức được minh họa với `(+ 5 1)` và `(* 5 2)` ở trên và, quan trọng hơn, vì việc đánh giá theo thứ tự bình thường trở nên phức tạp hơn nhiều để xử lý khi chúng ta rời khỏi phạm vi của các thủ tục có thể được mô hình hóa bằng cách thay thế. Mặt khác, việc đánh giá theo thứ tự bình thường có thể là một công cụ cực kỳ có giá trị, và chúng ta sẽ điều tra một số hệ quả của nó trong [Chương 3](Chapter-3.xhtml#Chapter-3) và [Chương 4](Chapter-4.xhtml#Chapter-4).^[Trong [Chương 3](Chapter-3.xhtml#Chapter-3) chúng ta sẽ giới thiệu *xử lý luồng*, đó là một cách để xử lý các cấu trúc dữ liệu dường như “vô hạn” bằng cách kết hợp một dạng đánh giá theo thứ tự bình thường hạn chế. Trong [4.2](4_002e2.xhtml#g_t4_002e2) chúng ta sẽ sửa đổi trình thông dịch Scheme để tạo ra một phiên bản Scheme theo thứ tự bình thường.]


## 1.1.6 Biểu Thức Điều Kiện và Mệnh Đề

Sức mạnh biểu đạt của lớp các thủ tục mà chúng ta có thể định nghĩa ở thời điểm này là rất hạn chế, vì chúng ta không có cách nào để thực hiện các bài kiểm tra và thực hiện các hoạt động khác nhau tùy thuộc vào kết quả của bài kiểm tra. Ví dụ, chúng ta không thể định nghĩa một thủ tục tính giá trị tuyệt đối của một số bằng cách kiểm tra xem số đó là dương, âm hay bằng không và thực hiện các thao tác khác nhau trong các trường hợp khác nhau theo quy tắc

$$\left| x \right|\; = \;\left\{ \begin{array}{lll}
x & {\;\text{nếu}} & {x > 0,} \\
0 & {\;\text{nếu}} & {x = 0,} \\
{- x} & {\;\text{nếu}} & {x < 0.} \\
\end{array} \right.$$

Cấu trúc này được gọi là *phân tích trường hợp*, và trong Lisp có một dạng đặc biệt để ghi chú phân tích trường hợp như vậy. Nó được gọi là `cond` (viết tắt của “điều kiện”), và nó được sử dụng như sau:

``` {.scheme}
(define (abs x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))))
```

Dạng tổng quát của một biểu thức điều kiện là

``` {.scheme}
(cond (⟨p₁⟩ ⟨e₁⟩)
      (⟨p₂⟩ ⟨e₂⟩)
      …
      (⟨pₙ⟩ ⟨eₙ⟩))
```

gồm ký hiệu `cond` theo sau bởi các cặp biểu thức trong dấu ngoặc đơn

``` {.scheme}
(⟨p⟩ ⟨e⟩)
```

được gọi là *các mệnh đề*. Biểu thức đầu tiên trong mỗi cặp là một *mệnh đề* – tức là một biểu thức mà giá trị của nó được hiểu là đúng hoặc sai.^[“Được hiểu là đúng hoặc sai” có nghĩa là: Trong Scheme, có hai giá trị được phân biệt bằng các hằng số `#t` và `#f`. Khi trình thông dịch kiểm tra giá trị của một mệnh đề, nó hiểu `#f` là sai. Bất kỳ giá trị nào khác đều được coi là đúng. (Do đó, việc cung cấp `#t` về mặt logic là không cần thiết, nhưng nó thuận tiện.) Trong cuốn sách này, chúng ta sẽ sử dụng các tên `đúng` và `sai`, được liên kết với các giá trị `#t` và `#f` tương ứng.]

Các biểu thức điều kiện được đánh giá như sau. Mệnh đề $\langle p_{1}\rangle$ được đánh giá trước tiên. Nếu giá trị của nó là sai, thì $\langle p_{2}\rangle$ được đánh giá. Nếu giá trị của $\langle p_{2}\rangle$ cũng là sai, thì $\langle p_{3}\rangle$ được đánh giá. Quá trình này tiếp tục cho đến khi tìm thấy một mệnh đề có giá trị là đúng, trong trường hợp đó trình thông dịch trả về giá trị của biểu thức *hậu quả* $\langle e\rangle$ tương ứng của