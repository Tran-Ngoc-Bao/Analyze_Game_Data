# Bài tập lớn IT4931 
## Thành viên nhóm
<table>
  <tr>
    <th>Họ tên</th>
    <th>MSSV</th>
    <th>Nhiệm vụ</th>
  </tr>
<tr>
  <td>Trần Ngọc Bảo (Trưởng nhóm)</td>
  <td>20215529</td>
  <td>Triền khai hệ thống, <br> Lưu trữ và xử lý dữ liệu</td>
</tr>
<tr>
  <td>Vũ Hồng Phước</td>
  <td>20204847</td>
  <td>Thu thập dữ liệu</td>
</tr>
<tr>
  <td>Nguyễn Ngọc Bình Dương</td>
  <td>20204734</td>
  <td>Thu thập dữ liệu</td>
</tr>
<tr>
  <td>Hà Duy Long</td>
  <td>20204841</td>
  <td>Viết báo cáo</td>
</tr>
<tr>
  <td>Trần Bách Lưu Đức</td>
  <td>20200180</td>
  <td>Viết báo cáo</td>
</tr>
</table>

## Giới thiệu bài tập lớn
<ul>
  <li>Tên đề tài: Lưu trữ và xử lý dữ liệu trò chơi điện tử trên điện thoại và máy tính bảng từ App store và Google play </li>
  <li>Thu thập dữ liệu game trên Google play và App store <strong> hàng tuần</strong></li>
  <li>Lưu trữ, phân tích, xử lí dữ liệu thu được</li>
  <li>Biểu diễn kết quả thu được dưới dạng các biểu đồ</li>
</ul>

## Cài đặt hệ thống
<ul>
  <li>Cài đặt <strong>VirtualBox</strong> <br>&emsp;Sau đó tạo 1 máy ảo ubuntu đóng vai trò là namenode (master)</li>
  <li>Cài đặt <strong>BeutifulSoup4, ssh-server, jdk-8</strong></li>
  <li>Cài đặt <strong>hadoop, spark, elasticsearch, kibana</strong> trên máy ảo</li>
  <li>Clone máy ảo tạo 2 máy ảo khác, đồng thời cấu hình lại, mỗi máy sẽ đóng vai trò là datanode (worker)</li>
</ul>

## Hướng dẫn sử dụng 
<ul>
  <li>Thu thập dữ liệu phân tán, đa luồng trên các máy ảo bằng <strong>BeautifulSoup4</strong> từ: <br>&emsp;App store (https://apps.apple.com/vn/genre/ios-tr%C3%B2-ch%C6%A1i/id6014?l=vi) <br>&emsp;Google play (https://play.google.com/store/games?device=phone&hl=vi-VN)</li>
  <li>Tạo mạng kết nối giữa các máy ảo nhờ <strong>VirtualBox và ssh-server</strong></li>
  <li>Đẩy dữ liệu thu thập được vào <strong>hdfs của hadoop</strong></li>
  <li>Chạy các đoạn code trong phần source_code nhờ <strong>pyspark</strong> để phân tích, xử lí dữ liệu</li>
  <li>Đẩy dữ liệu đã được lọc lên <strong>elasticsearch</strong></li>
  <li>Biểu diễn dữ liệu một cách trực quan bằng <strong>kibana</strong></li>
  <li>XEM CHI TIẾT TRONG BÁO CÁO BÀI TẬP LỚN</li>
</ul>

## Báo cáo bài tập lớn
<ul>
  <li>Báo cáo</li>
  <li>Slides</li>
</ul>
