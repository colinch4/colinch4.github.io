---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 그리드 뷰"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

## 소개

Swift를 사용하여 이미지 그리드 뷰를 구현하는 방법을 알아보겠습니다. 이 예제에서는 `UICollectionView`를 사용하여 이미지들을 그리드 형태로 보여줄 것입니다. 각 이미지를 탭하면 확대된 이미지가 모달 형태로 표시됩니다.

## 구현

먼저, `UICollectionView`를 생성해야 합니다. 이를 위해 `UICollectionViewDataSource`와 `UICollectionViewDelegate` 프로토콜을 구현해야 합니다.

```swift
import UIKit

class ImageGridViewController: UIViewController, UICollectionViewDataSource, UICollectionViewDelegate {
    
    // 이미지들의 배열
    let images = [UIImage(named: "image1"), UIImage(named: "image2"), UIImage(named: "image3"), UIImage(named: "image4"), UIImage(named: "image5")]

    // 이미지 그리드 뷰
    @IBOutlet weak var collectionView: UICollectionView!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // collectionView의 dataSource와 delegate를 self로 설정
        collectionView.dataSource = self
        collectionView.delegate = self
        
        // collectionView의 레이아웃을 설정
        // 각 셀의 크기와 간격을 조정할 수 있습니다.
        let layout = UICollectionViewFlowLayout()
        let itemSize = UIScreen.main.bounds.width / 4
        layout.itemSize = CGSize(width: itemSize, height: itemSize)
        layout.minimumInteritemSpacing = 0
        layout.minimumLineSpacing = 0
        collectionView.collectionViewLayout = layout
    }
    
    // MARK: - UICollectionViewDataSource
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return images.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "ImageCell", for: indexPath) as! ImageCell
        
        // 이미지를 설정
        cell.imageView.image = images[indexPath.item]
        
        return cell
    }
    
    // MARK: - UICollectionViewDelegate
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        let selectedImage = images[indexPath.item]
        
        // 확대된 이미지를 표시할 ViewController를 생성하고 이미지를 전달
        let imageDetailVC = ImageDetailViewController(image: selectedImage)
        
        // 모달 형태로 표시
        self.present(imageDetailVC, animated: true, completion: nil)
    }
}
```

이제 `UICollectionViewCell`을 생성해야 합니다. 이 셀은 이미지를 표시하기 위한 `UIImageView`가 포함된 뷰입니다.

```swift
import UIKit

class ImageCell: UICollectionViewCell {
    @IBOutlet weak var imageView: UIImageView!
}
```

마지막으로, 확대된 이미지를 표시할 ViewController를 생성해야 합니다.

```swift
import UIKit

class ImageDetailViewController: UIViewController {
    let imageView = UIImageView()

    init(image: UIImage?) {
        super.init(nibName: nil, bundle: nil)
        
        if let image = image {
            imageView.image = image
        }
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지뷰를 뷰에 추가
        imageView.frame = self.view.frame
        imageView.contentMode = .scaleAspectFit
        self.view.addSubview(imageView)
    }
}
```

## 결과

이미지 그리드 뷰를 실행하면, 화면에 이미지들이 4x4 그리드로 표시됩니다. 각 이미지를 탭하면 확대된 이미지가 모달 창으로 표시됩니다.

![ImageGridView](image.png)

## 참고 자료

- [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview)
- [UICollectionViewDataSource](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource)
- [UICollectionViewDelegate](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate)