#giải pháp
#1. Sử dụng List để lưu đơn hàng
#2. Các phương thức cần sử dụng: append, pop, strip, upper, split
#3. Kiểm tra dữ liệu hợp lệ: menu hợp lệ, vị trí hợp lệ, mã đơn hàng không trống

order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")

    main_choice = input("Nhập lựa chọn của bạn: ").strip()

    match main_choice:
        case "1":
            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                print("\nDanh sách đơn hàng hiện tại:")
                for index, order in enumerate(order_list, start=1):
                    print(f"{index}. {order}")

        case "2":
            while True:
                print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
                print("1. Thêm đơn hàng mới")
                print("2. Sửa đơn hàng theo vị trí")
                print("3. Xóa đơn hàng theo vị trí")
                print("4. Quay lại menu chính")

                update_choice = input("Nhập lựa chọn của bạn: ").strip()

                match update_choice:
                    case "1":
                        order_code = input("Nhập mã đơn hàng: ").strip().upper()
                        order_status = input("Nhập trạng thái đơn hàng: ").strip().upper()
                        new_order = f"{order_code} - {order_status}"
                        order_list.append(new_order)
                        print("Thêm đơn hàng thành công!")

                    case "2":
                        position = input("Nhập vị trí cần sửa: ").strip()

                        if not position.isdigit():
                            print("Vị trí không hợp lệ!")
                            continue

                        index = int(position) - 1

                        if 0 <= index < len(order_list):
                            new_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                            new_status = input("Nhập trạng thái mới: ").strip().upper()
                            order_list[index] = f"{new_code} - {new_status}"
                            print("Cập nhật đơn hàng thành công!")

                        else:
                            print("Không tồn tại đơn hàng ở vị trí này!")

                    case "3":
                        position = input("Nhập vị trí cần xóa: ").strip()

                        if not position.isdigit():
                            print("Vị trí không hợp lệ!")
                            continue

                        index = int(position) - 1

                        if 0 <= index < len(order_list):
                            deleted_order = order_list.pop(index)
                            print(f"Đã xóa đơn hàng: {deleted_order}")

                        else:
                            print("Không tồn tại đơn hàng ở vị trí này!")

                    case "4":
                        break

                    case _:
                        print("Lựa chọn không hợp lệ")

        case "3":
            pending_count = 0
            delivering_count = 0
            completed_count = 0
            cancelled_count = 0

            for order in order_list:
                parts = order.split(" - ")

                if len(parts) == 2:
                    status = parts[1]
                    match status:
                        case "PENDING":
                            pending_count += 1

                        case "DELIVERING":
                            delivering_count += 1

                        case "COMPLETED":
                            completed_count += 1

                        case "CANCELLED":
                            cancelled_count += 1

            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
            print(f"PENDING: {pending_count}")
            print(f"DELIVERING: {delivering_count}")
            print(f"COMPLETED: {completed_count}")
            print(f"CANCELLED: {cancelled_count}")
            print(f"Tổng số đơn hàng: {len(order_list)}")

        case "4":
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")