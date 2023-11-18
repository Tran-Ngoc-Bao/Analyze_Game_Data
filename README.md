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
  <li>Thu thập dữ liệu từ 100 game trên Google play và 100 game trên App store</li>
  <li>Lưu trữ, phân tích, xử lí dữ liệu thu được</li>
  <li>Biểu diễn kết quả thu được dưới dạng các biểu đồ</li>
</ul>

## Cài đặt hệ thống
<table>
  <tr>
    <th>Các phần mềm cần cài đặt</th>
    <th>Link hướng dẫn (tham khảo)</th>
  </tr>
  <tr>
    <td>BeatifulSoup4</td>
    <td>https://linux.how2shout.com/how-to-install-beautifulsoup-python-module-in-ubuntu-linux/</td>
  </tr>
    <td>VirtualBox: 1 máy ảo ubuntu 14 (master) <br> (Sau khi tải xong hết sẽ clone tạo 2 máy slave)</td>
    <td>https://www.youtube.com/watch?v=ngJQPt-xEeo&t=560s</td>
  </tr>
  <tr>
    <td>java 8 cho ubuntu 14</td>
    <td>https://askubuntu.com/questions/464755/how-to-install-openjdk-8-on-14-04-lts</td>
  </tr>
  <tr>
    <td>openssh-server</td>
    <td></td>
  </tr>
  <tr>
    <td>hadoop cluster</td>
    <td>https://viblo.asia/p/cung-thiet-lap-multi-node-cluster-trong-hadoop-2x-nao-5pPLkxXdVRZ</td>
  </tr>
  <tr>
    <td>spark cluster</td>
    <td>https://www.youtube.com/watch?v=9UpnWyy1M34&t=602s</td>
  </tr>
  <tr>
    <td>elasticsearch cluster</td>
    <td>https://123host.vn/tailieu/kb/dedicated-server/huong-dan-cai-dat-elasticsearch-cluster-tren-ubuntu-20-04.html</td>
  </tr>
  <tr>
    <td>kibana <br> (sau khi tải xong sẽ clone tạo 2 máy slave)</td>
    <td>https://www.unixmen.com/install-kibana-ubuntu-14-04/#google_vignette</td>
  </tr>
</table>

## Hướng dẫn sử dụng 
<ul>
  <li>Thu thập dữ liệu trên: <br> App store (https://apps.apple.com/vn/genre/ios-tr%C3%B2-ch%C6%A1i/id6014?l=vi) <br> Google play (https://play.google.com/store/games?device=phone&hl=vi-VN) <br> Bằng BeautifulSoup4</li>
  <li>Cài đặt hệ thống như trên</li>
  <li>Tạo mạng kết nối giữa các máy ảo nhờ VirtualBox và ssh server</li>
  <li>Đẩy dữ liệu từ phần data vào hdfs của hadoop</li>
  <li>Chạy các đoạn code trong phần source_code nhờ pyspark</li>
  <li>Biểu diễn dữ liệu một cách trực quan bằng elasticsearch, kibana</li>
</ul>

## Báo cáo bài tập lớn
<ul>
  <li>Báo cáo</li>
  <li>Slides</li>
</ul>
