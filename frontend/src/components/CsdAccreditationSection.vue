<template>
  <section class="accreditation">
    <div class="container">
      <div class="row">
        <div class="col-12 col-lg-4">
          <div class="accreditation__wrapper">
            <h2 v-html="$static.allAccreditationInfo.edges[0].node.title"/>
            <p class="accreditation__description" v-html="$static.allAccreditationInfo.edges[0].node.text"/>
            <csd-slider-arrows
              @prev="handleSlidePrev"
              @next="handleSlideNext"
              :class="['d-none ml-auto mt-auto d-lg-flex']"
            />
          </div>
        </div>
        <div class="offset-lg-1 col-12 col-lg-7">
          <div class="swiper swiper-certificates">
            <div class="swiper-wrapper pb-1" v-if="$static.allCertificates.edges.length > 0">
              <template v-for="{node} in $static.allCertificates.edges">
                <div class="swiper-slide">
                  <div class="certificate">
                    <div
                      class="certificate__image"
                      :style="{backgroundImage: `url('${normalizeImageSrc(node.image)}')`}"
                    />
                    <p class="certificate__name">{{ node.label }}</p>
                  </div>
                </div>
              </template>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <csd-slider-arrows
            @prev="handleSlidePrev"
            @next="handleSlideNext"
            :class="['mx-auto d-lg-none']"
          />
        </div>
      </div>
    </div>
  </section>
</template>
<static-query>
query {
  allCertificates {
    edges {
      node {
        id
        label
        image
      }
    }
  }
  allAccreditationInfo {
    edges {
      node {
        title
        text
      }
    }
  }
}
</static-query>
<script>
import Swiper from 'swiper'
import 'swiper/swiper.scss'
import CsdSliderArrows from './CsdSliderArrows'
import windowSizeMixin from '../mixins/windowSizeMixin'
import normalizeImageSrc from '../mixins/normalizeImageSrc'

export default {
  name: 'CsdAccreditationSection',
  mixins: [windowSizeMixin, normalizeImageSrc],
  components: { CsdSliderArrows },
  data() {
    return {
      swiper: null
    }
  },
  methods: {
    handleSlidePrev() {
      this.swiper.slidePrev()
    },
    handleSlideNext() {
      this.swiper.slideNext()
    }
  },
  mounted() {
    this.swiper = new Swiper('.swiper-certificates', {
      speed: 400,
      loop: true,
      slidesPerView: 2,
      spaceBetween: 10,
      breakpoints: {
        425: {
          slidesPerView: 3,
        },
        576: {
          slidesPerView: 2,
          spaceBetween: 20
        },
        1400: {
          slidesPerView: 3,
          spaceBetween: 20
        }
      }
    })
  }
}
</script>
