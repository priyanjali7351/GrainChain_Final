"use client"

import dynamic from "next/dynamic"

const FoodMap = dynamic(() => import("@/components/map/food-map"), {
  ssr: false,
  loading: () => <div>Loading map...</div>,
})

export default FoodMap
